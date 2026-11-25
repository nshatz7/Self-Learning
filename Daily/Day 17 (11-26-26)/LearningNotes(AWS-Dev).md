# Course 8: Adding Asynchronous Processing

In synchronous architectures, if a slow downstream service stalls or crashes, upstream callers time out or fail. This course introduces asynchronous messaging and workflow orchestration using **Amazon SQS**, **Amazon SNS**, **Amazon EventBridge**, and **AWS Step Functions** so services stay decoupled, resilient, and independently scalable.

---

## 1. Amazon SQS (Simple Queue Service): Decoupling & Buffering

Amazon SQS is a durable, fully managed poll-based message queue (messages up to 256 KB, retained from 1 minute up to 14 days, default 4 days). Producers write messages to the queue, and consumers pull them at their own pace without losing work during traffic spikes or consumer downtime.

### Standard vs. FIFO Queues

| Feature | Standard Queue | FIFO Queue (`.fifo`) |
| :--- | :--- | :--- |
| **Throughput** | Nearly unlimited transactions per second (TPS). | Higher throughput available with high-throughput mode; supports Message Group IDs for parallel ordered groups. |
| **Ordering** | Best-effort ordering (messages may arrive out of order). | Strict First-In, First-Out ordering within each `MessageGroupId`. |
| **Delivery / Deduplication** | At-least-once delivery (occasional duplicate messages can occur). | Exactly-once processing within the deduplication window using `MessageDeduplicationId` or content-based deduplication. |
| **Best Use Cases** | High-volume background jobs where occasional duplicates or out-of-order tasks are acceptable. | Financial ledgers, inventory updates, or state transitions per entity (`MessageGroupId = order-123`) where order matters. |

### Visibility Timeout & Polling Mechanics

* **Visibility Timeout:** When a consumer reads a message, SQS does not delete it immediately—it hides it from other consumers for a visibility timeout period (default 30 seconds, adjustable up to 12 hours).
  * If the consumer finishes in time, it explicitly calls `DeleteMessage`.
  * If the consumer crashes or takes longer than the visibility timeout, the message becomes visible again and another consumer picks it up. *(Best practice: set visibility timeout to at least 6x your Lambda function's timeout when using SQS event source mappings.)*
* **Long Polling (`WaitTimeSeconds` up to 20s):** Instead of short polling (which returns empty responses immediately and wastes API requests), long polling holds the connection open until a message arrives or 20 seconds elapse—reducing empty responses and lowering cost.

---

## 2. Amazon SNS (Simple Notification Service) & The Fan-Out Pattern

While SQS is a pull-based queue for buffering work, Amazon SNS is a push-based publish/subscribe (pub/sub) service. Producers publish once to an SNS Topic, and SNS pushes the message immediately to subscribed endpoints (SQS queues, Lambda functions, HTTP/S webhooks, SMS, Email).

### Why Combine SNS + SQS (Fan-Out Pattern)?

If a single Lambda function publishes an event to an SNS topic that has three SQS queues subscribed to it (e.g., `BillingQueue`, `InventoryQueue`, `NotificationQueue`), every queue receives its own copy of the message simultaneously:

* **Independent Scaling & Failure Isolation:** If `NotificationQueue`'s consumer fails or slows down, `BillingQueue` and `InventoryQueue` keep processing unaffected.
* **Message Filtering:** Subscribers can attach SNS Subscription Filter Policies so a consumer only receives messages matching specific attributes (e.g., `{"order_type": ["international"]}`) rather than filtering every event in application code.

---

## 3. Amazon EventBridge: Event-Driven Routing

Amazon EventBridge is a serverless event bus designed for routing events between AWS services, custom applications, and SaaS partners.

### SNS vs. EventBridge

* **SNS:** Ideal for high-throughput pub/sub fan-out, mobile/SMS/email alerts, and simple message broadcasting.
* **EventBridge:** Excels at content-based event routing using rich Event Rules and Event Patterns that match fields inside JSON event payloads (e.g., routing only when `detail.amount > 1000` and `detail.region == "us-east-1"`), plus built-in **EventBridge Pipes** (point-to-point filtering/enrichment between sources like SQS/DynamoDB Streams and targets) and **EventBridge Scheduler** (cron/one-time schedules at massive scale).

---

## 4. AWS Step Functions: Orchestrating Multi-Step Workflows

Queues and topics move single messages, but real business workflows often involve multiple steps, branching logic, parallel execution, human approvals, and retries (e.g., Reserve Inventory $\rightarrow$ Charge Card $\rightarrow$ Create Shipment $\rightarrow$ Send Receipt, with compensating rollbacks if a step fails).

AWS Step Functions coordinates distributed components using state machines defined in **Amazon States Language (ASL)**:

* **Standard Workflows:** Designed for long-running (up to 1 year), durable workflows where exactly-once execution and full auditability/visual execution history matter.
* **Express Workflows:** Designed for high-event-rate, short-duration workflows (up to 5 minutes), priced by request count and duration rather than state transitions—great for high-volume data ingestion or IoT pipelines.
* **Built-In Resilience (`Retry` and `Catch`):** Instead of writing retry loops and try/catch blocks inside every Lambda function, Step Functions declares `Retry` policies (with exponential backoff) and `Catch` fallback branches directly in the workflow definition.

```json
{
  "StartAt": "ChargePayment",
  "States": {
    "ChargePayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ChargePaymentFn",
      "Retry": [
        {
          "ErrorEquals": ["States.Timeout", "PaymentGatewayThrottled"],
          "IntervalSeconds": 2,
          "BackoffRate": 2.0,
          "MaxAttempts": 3
        }
      ],
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "RefundOrAlert"
        }
      ],
      "Next": "FulfillOrder"
    },
    "FulfillOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:FulfillOrderFn",
      "End": true
    },
    "RefundOrAlert": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:NotifyFailureFn",
      "End": true
    }
  }
}
```

---

## Key Exam & Best-Practice Takeaways

* **SQS** = pull-based queue for buffering/decoupling; **SNS** = push-based pub/sub for fan-out to multiple consumers; **EventBridge** = content-based event router across AWS/SaaS events; **Step Functions** = state machine orchestrator for multi-step workflows.
* Use **FIFO queues** when ordering within a `MessageGroupId` and deduplication are required; use **Standard queues** for maximum throughput where consumers are idempotent.
* Set your SQS queue's **visibility timeout** higher than your consumer's processing time (and Lambda timeout) so messages don't reappear mid-execution and cause duplicate work.
