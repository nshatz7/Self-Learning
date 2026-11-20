# Course 3: Building Your First Serverless API

This course transitions from theory to hands-on serverless engineering. You learn how **Amazon API Gateway** acts as the front door for incoming HTTP traffic and triggers **AWS Lambda** to execute stateless backend business logic—without provisioning or patching a single server.

---

## 1. End-to-End Request Lifecycle

When a client (browser, mobile app, or `curl`) calls a serverless API, the request moves through a managed pipeline:

1. **Client Request:** Sends an HTTP request (e.g., `GET /items/42` or `POST /orders`) to an API Gateway endpoint URL.
2. **Routing & Validation:** API Gateway matches the HTTP method and resource path, enforces authorization/throttling rules, and converts the HTTP request into a structured JSON event payload.
3. **Synchronous Invocation:** API Gateway invokes the target Lambda function synchronously (`RequestResponse` invocation type) and waits for a response.
4. **Execution:** Lambda spins up (or reuses) an execution environment, passes the `event` and `context` objects to your handler function, and runs your business logic.
5. **Response Mapping:** Lambda returns a formatted JSON response containing an HTTP `statusCode`, `headers`, and stringified `body`, which API Gateway forwards back to the client.

---

## 2. Anatomy of an AWS Lambda Function

Every Lambda function requires three core components:
* **Code (Handler):** The entry point function executed by AWS Lambda.
* **Configuration:** Memory, timeout, runtime, and environment variables.
* **Execution Role:** An IAM role defining what AWS services the function can call.

### The Handler Signature (Python Example)

```python
import json

def lambda_handler(event, context):
    # 1. Extract data from the API Gateway proxy event
    http_method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method")
    path_params = event.get("pathParameters") or {}
    query_params = event.get("queryStringParameters") or {}
    
    # Body arrives as a JSON string in proxy integrations
    raw_body = event.get("body")
    payload = json.loads(raw_body) if raw_body else {}

    # 2. Check remaining execution time via context
    remaining_ms = context.get_remaining_time_in_millis()

    # 3. Return the required API Gateway proxy response format
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Required for browser CORS
        },
        "body": json.dumps({
            "message": "Request processed successfully",
            "itemId": path_params.get("id"),
            "remainingTimeMs": remaining_ms
        })
    }
```

### Understanding `event` vs. `context`

* **`event` (dict/JSON):** Contains the data that triggered the function—HTTP headers, query strings, path parameters, request body, and caller identity.
* **`context` (object):** Provides runtime metadata provided by AWS Lambda, including `function_name`, `aws_request_id` (critical for tracing logs), `memory_limit_in_mb`, and `get_remaining_time_in_millis()`.

---

## 3. Amazon API Gateway: API Types & Integrations

API Gateway supports multiple API styles, with **HTTP APIs** and **REST APIs** being the primary choices for web backends:

| Feature | HTTP API (API Gateway v2) | REST API (API Gateway v1) |
| :--- | :--- | :--- |
| **Latency & Cost** | Lower latency; up to ~70% cheaper. | Higher cost; more feature-heavy. |
| **Authorization** | OIDC / OAuth 2.0 (JWT), Lambda authorizers, IAM. | Cognito User Pools, Lambda authorizers, IAM, API Keys + Usage Plans. |
| **Advanced Features** | Native CORS support, automatic deployments. | Request/response VTL mapping templates, edge-optimized endpoints, caching, WAF integration, mock integrations. |
| **When to Choose** | Standard modern JSON/Lambda microservices where speed and cost matter most. | Enterprise APIs needing API keys, request validation schemas, response caching, or legacy XML/VTL transformations. |

### Proxy vs. Non-Proxy (Custom) Integration

* **Lambda Proxy Integration (Standard):** API Gateway passes the entire raw HTTP request directly into Lambda's `event` object untouched, and Lambda is responsible for returning the exact `{ statusCode, headers, body }` structure.
* **Non-Proxy Integration:** You use Velocity Template Language (VTL) inside API Gateway to reshape incoming payloads before Lambda sees them and transform Lambda's output into custom HTTP status codes or XML/JSON formats.

---

## 4. Stages, Deployments, and CORS

* **Stages (`dev`, `staging`, `prod`):** API Gateway changes do not go live until you deploy the API to a named stage (HTTP APIs offer a `$default` auto-deploy stage). Each stage receives its own invoke URL:
  ```text
  https://{api-id}.execute-api.{region}.amazonaws.com/{stage}/{resource}
  ```
* **Stage Variables:** Key-value pairs attached to a stage (e.g., `lambdaAlias=prod`) that let one API configuration route traffic to different backend Lambda versions depending on the stage.
* **CORS (Cross-Origin Resource Sharing):** When a frontend web app on `https://app.example.com` calls an API on `execute-api.amazonaws.com`, browsers send a preflight `OPTIONS` request. You must configure CORS headers (`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`) on API Gateway and return `Access-Control-Allow-Origin` from Lambda proxy responses.

---

## 5. Defining Your First API with AWS SAM

Rather than clicking through the console, developers define API Gateway + Lambda together in a `template.yaml` file using **AWS SAM** (Serverless Application Model):

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: First Serverless API

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.12
      Events:
        HelloGetApi:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

Deploying takes three CLI commands:

```bash
sam validate -> sam build -> sam deploy --guided
```

---

## Key Exam & Best-Practice Takeaways

* **Two Types of IAM Policies on Lambda:**
  1. **Execution Role:** Grants Lambda permission to call other AWS services (e.g., write to CloudWatch Logs or DynamoDB).
  2. **Resource-Based Policy:** Grants external services (like API Gateway) permission to invoke your Lambda function.
* **502 Bad Gateway Errors:** If a Lambda proxy function returns a plain Python dictionary without `statusCode` and a JSON-stringified `body`, API Gateway throws an HTTP `502 Bad Gateway` (`"Malformed Lambda proxy response"`).
* **API Selection:** Choose **HTTP API** over **REST API** when you only need simple JWT/IAM auth and want lower latency/cost; choose **REST API** when you need API keys, usage plans, request caching, or AWS WAF.

