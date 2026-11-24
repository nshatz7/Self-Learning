# Course 5: Testing and Error Handling

This final course of Phase 1 teaches you how to validate serverless applications locally before deploying to AWS, and how to build resilient error-handling pipelines so failed events are captured, diagnosed, and reprocessed rather than silently lost.

---

## 1. Local Testing with the AWS SAM CLI

Deploying to AWS on every code tweak slows down feedback loops. The **AWS Serverless Application Model (SAM) CLI** uses local Docker containers to emulate the exact AWS Lambda execution runtime and API Gateway locally on your machine.

### Essential SAM Local Commands

* **Generate Mock Event Payloads (`sam local generate-event`):** Produces realistic JSON event structures for AWS services (API Gateway, S3, SQS, DynamoDB) so you don't have to guess schema formats:
  ```bash
  sam local generate-event apigateway aws-proxy --method POST --path /orders --body '{"item":"laptop"}' > event.json
  ```
* **Single Function Invocation (`sam local invoke`):** Runs a single Lambda function inside a Docker container using a sample event payload, outputting CloudWatch-style logs (`START`, `END`, `REPORT` with billed duration and max memory used):
  ```bash
  sam local invoke CreateOrderFunction -e event.json
  ```
* **Local API Server (`sam local start-api`):** Spins up a local HTTP server (default `http://127.0.0.1:3000`) simulating API Gateway routes defined in `template.yaml`. Changes to interpreted languages (Python, Node.js) reload automatically without rebuilding.
* **Local Lambda Endpoint (`sam local start-lambda`):** Starts a local endpoint mimicking the AWS Lambda Invoke API, allowing automated integration tests using the standard AWS SDK:
  ```python
  boto3.client("lambda", endpoint_url="http://127.0.0.1:3001")
  ```
* **Rapid Cloud Sync (`sam sync --watch`):** When testing integrations that cannot be fully emulated locally (like IAM permissions or Step Functions), `sam sync` bypasses full CloudFormation change sets to push code updates directly to AWS in seconds.

### Unit Testing Best Practices

* **Separate Business Logic from the Handler:** Keep core domain logic in pure functions independent of `event` and `context` objects so you can run fast unit tests (`pytest`, `jest`) without spinning up Docker.
* **Mock AWS SDK Calls:** Use libraries like **Moto** (Python) or **aws-sdk-client-mock** (Node.js) to simulate DynamoDB or S3 calls in unit tests without incurring cloud costs or latency.

---

## 2. How AWS Lambda Handles Errors by Invocation Model

Error handling in Lambda depends entirely on how the function is invoked:

### A. Synchronous Invocations (API Gateway, SDK `RequestResponse`)
* **Behavior:** Lambda does not automatically retry failed executions. It immediately returns the error payload (or stack trace) to the caller.
* **Responsibility:** The caller (client app or API Gateway) must handle the HTTP `4xx`/`5xx` error and implement retry logic with exponential backoff.

### B. Asynchronous Invocations (S3, SNS, EventBridge, SDK `Event`)
* **Behavior:** AWS places the event into an internal queue and returns an immediate `202 Accepted` to the caller.
* **Built-in Retries:** If the function throws an unhandled exception or times out, Lambda automatically retries up to **2 times** (total of 3 attempts) with built-in backoff delays (1 minute after first failure, 2 minutes after second failure).
* **Idempotency Requirement:** Because Lambda may deliver the exact same event more than once during retries, your function logic must be **idempotent** (e.g., checking a DynamoDB conditional write before processing an order).

### C. Event Source Mappings / Poll-Based (SQS, Kinesis, DynamoDB Streams)
* **Behavior:** Lambda polls batches of records from the stream or queue.
* **Stream Behavior (Kinesis / DynamoDB Streams):** By default, a failing record blocks the entire shard until it succeeds or expires (up to 7 days). To prevent "poison pill" records from halting processing, configure:
  * **`BisectBatchOnFunctionError`:** Splits a failing batch in half recursively to isolate the single bad record.
  * **`MaximumRetryAttempts` & `MaximumRecordAgeInSeconds`:** Caps retries and forwards expired/failed records to an On-Failure Destination (SQS or SNS).
* **SQS Partial Batch Responses (`ReportBatchItemFailures`):** Normally, if 1 message out of a batch of 10 fails, Lambda returns the entire batch of 10 back to the queue to be reprocessed. Enabling `FunctionResponseTypes: [ReportBatchItemFailures]` lets your code return only the specific failed `itemIdentifiers` so successful messages are deleted immediately.

---

## 3. Dead-Letter Queues (DLQs) vs. Lambda Destinations

When an asynchronous Lambda function exhausts all retry attempts, you must capture the failed event to prevent silent data loss. AWS provides two mechanisms—**Lambda Destinations** is the modern standard:

| Feature | Dead-Letter Queue (DLQ) | Lambda Destinations (Preferred) |
| :--- | :--- | :--- |
| **Supported Targets** | Amazon SQS or Amazon SNS only. | SQS, SNS, another Lambda function, or Amazon EventBridge. |
| **Trigger Conditions** | Triggers only on failure. | Separate routing for `OnSuccess` and `OnFailure`. |
| **Payload Sent** | Sends only the original event payload (error stack trace is omitted; requires digging into CloudWatch Logs). | Sends a rich Invocation Record JSON containing the original `requestPayload`, the `responsePayload` (exact error message/stack trace), and metadata. |
| **Stream Support** | Not supported for Kinesis/DynamoDB Streams. | Supported as an `OnFailure` destination for stream event source mappings. |

### Configuring Destinations in AWS SAM (`template.yaml`)

```yaml
ProcessOrderFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: orders/
    Handler: app.lambda_handler
    Runtime: python3.12
    EventInvokeConfig:
      MaximumRetryAttempts: 2
      MaximumEventAgeInSeconds: 3600
      DestinationConfig:
        OnFailure:
          Type: SQS
          Destination: !GetAtt FailedOrdersQueue.Arn
```

> **Note:** Remember that Lambda's Execution Role must explicitly be granted `sqs:SendMessage` permission on the target queue ARN.

---

## 4. API Gateway Request Validation & Error Mapping

Catching invalid client payloads at the API Gateway layer saves money and compute time because malformed requests are rejected before invoking Lambda:

* **Request Validators:** Attach a JSON Schema (Model) to your API Gateway method to validate required headers, query parameters, and JSON body fields. Invalid requests automatically return `HTTP 400 Bad Request` at the gateway.
* **Common API Gateway HTTP Status Codes to Know for the Exam:**
  * **`400 Bad Request`:** Failed request validation or malformed JSON payload.
  * **`403 Forbidden`:** Invalid/missing API Key, WAF block, or failed IAM/Cognito authorization.
  * **`429 Too Many Requests`:** Client exceeded API Gateway throttling rate/burst limits (or Usage Plan quota).
  * **`502 Bad Gateway`:** Lambda returned an improperly formatted proxy response (e.g., missing `statusCode` or non-stringified `body`) or crashed unhandled.
  * **`504 Gateway Timeout`:** Backend Lambda function exceeded API Gateway's hard **29-second** integration timeout limit.

---

## Key Exam & Best-Practice Takeaways

* **Prefer Lambda Destinations over DLQs** for asynchronous error handling because Destinations capture both the request payload and the error stack trace, and support EventBridge and Lambda targets.
* **API Gateway has a hard maximum integration timeout of 29 seconds** (even though Lambda can run up to 15 minutes). Tasks taking longer than 29 seconds behind an API must switch to an asynchronous pattern (return `202 Accepted` immediately and process via SQS/Step Functions).
* **For SQS triggers**, return `{"batchItemFailures": [{"itemIdentifier": msg_id}]}` with `ReportBatchItemFailures` enabled so one bad message doesn't force successful messages in the same batch to be reprocessed.
