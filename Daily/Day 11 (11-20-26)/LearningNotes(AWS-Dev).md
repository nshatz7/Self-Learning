# Course 2: Introduction to Being an AWS Developer

This course shifts your mindset from traditional server-based programming to cloud-native engineering. You learn how an AWS developer's responsibilities differ from legacy software engineering, how to evaluate trade-offs across AWS compute options, and how to leverage AI-assisted developer tools.

---

## 1. The Cloud-Native Developer Mindset

In traditional on-premises development, developers hand code off to an operations team that manages physical servers, OS patches, and scaling. On AWS, infrastructure is code, and developers own the application lifecycle end-to-end.

### Monolithic vs. Microservices Architecture

* **Monolithic Applications:** All business logic (authentication, billing, inventory, search) runs inside a single codebase and deploys as one unit.
  * **Drawback:** A memory leak or traffic spike in one module can bring down the entire application, and scaling requires duplicating the whole monolith.
* **Microservices Architecture:** The application is decomposed into small, independent services (e.g., an Order Service, a Payment Service, a Notification Service) that communicate over APIs or asynchronous events.
  * **Advantage:** Each service can be written in a different language, scaled independently, and deployed without risking the rest of the system.

### Stateful vs. Stateless Design

To scale horizontally across multiple servers or serverless containers, cloud-native applications must be stateless:

* **Stateful (Anti-pattern for cloud scaling):** Storing user sessions, shopping carts, or uploaded files on the local disk or in-memory RAM of a specific compute instance. If that instance terminates or a load balancer routes the next request to a different instance, the data is lost.
* **Stateless (Cloud-native standard):** Compute nodes process a request and forget it. Any persistent state or session data is externalized to dedicated managed stores like Amazon DynamoDB (session/database state), Amazon ElastiCache (in-memory caching), or Amazon S3 (files/objects).

---

## 2. Evaluating AWS Compute Platforms & Trade-Offs

A core skill tested heavily on the DVA-C02 exam is choosing the right compute model based on cost, performance, operational overhead, and scalability.

| Compute Option | Primary AWS Services | Operational Overhead | Scaling Behavior | Best Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Virtual Machines (IaaS)** | Amazon EC2 | **High** – You manage OS patches, security updates, runtime, and scaling rules. | Minutes (via Auto Scaling Groups). | Legacy apps, custom OS kernels, long-running stateful workloads, predictable 24/7 traffic. |
| **Containers (CaaS)** | Amazon ECS / EKS (with AWS Fargate or EC2) | **Medium** – You package the app + dependencies into Docker images; Fargate eliminates server management. | Seconds to minutes. | Microservices needing custom runtimes, specific libraries, or long-running processes without 15-minute execution caps. |
| **Serverless Functions (FaaS)** | AWS Lambda | **Lowest** – AWS manages servers, OS, runtime patching, and high availability; you only upload code. | Instantaneous (scales per-request from 0 to thousands). | Event-driven APIs, background jobs, file processing, spiky/unpredictable traffic (pay-per-millisecond). |

### Key Trade-Off Dimensions

1. **Execution Duration:** AWS Lambda has a hard maximum timeout of 15 minutes per invocation. Tasks exceeding 15 minutes belong on AWS Fargate, EC2, or AWS Batch.
2. **Cold Starts vs. Idle Cost:** Lambda costs `$0` when idle, but infrequent functions may experience a brief initialization delay ("cold start"). EC2 and Fargate incur continuous hourly charges even at 0% CPU, but respond immediately without cold starts.
3. **Vendor Lock-in vs. Velocity:** Containers (Docker on ECS/EKS) offer maximum portability across clouds and local machines, whereas Lambda maximizes development speed via native event triggers (S3, DynamoDB Streams, SQS).

---

## 3. Core Cloud-Native Design Principles

* **Loose Coupling:** Components interact through well-defined interfaces (REST APIs, message queues, event buses) rather than direct hardcoded dependencies. If a downstream service goes offline, messages queue up safely instead of crashing the upstream caller.
* **Design for Failure:** Assume hardware will fail, networks will drop packets, and downstream APIs will throttle requests. Developers build resilience directly into code using retries with exponential backoff and jitter, timeouts, and fallback paths.
* **Idempotency:** Designing operations so that executing the exact same request multiple times produces the same result as executing it once (e.g., attaching a unique `request_id` to a payment charge so a network retry doesn't double-bill a customer).

---

## 4. AI-Assisted Cloud Development on AWS

Modern AWS developer workflows integrate generative AI assistants directly into the IDE and CLI to accelerate boilerplate creation, debugging, and AWS service configuration:

* **Amazon Q Developer / Kiro:** AI-powered coding companions integrated into VS Code, JetBrains, and the terminal.
* **Developer Use Cases:**
  * Generating AWS SDK calls (e.g., Boto3 pagination or DynamoDB query expressions) and Infrastructure-as-Code templates (SAM/CDK).
  * Explaining unfamiliar IAM permission errors (`AccessDeniedException`) and suggesting least-privilege policy fixes.
  * Generating unit tests, refactoring legacy code blocks, and scanning code for hardcoded secrets or security vulnerabilities.

---

## Key Exam & Best-Practice Takeaways

* Stateless compute + managed external state is the golden rule of horizontal scaling on AWS.
* Choose **Lambda** for event-driven, short-lived tasks (under 15 minutes) with spiky traffic; choose **Fargate/ECS** for containerized microservices or long-running processes without server management; choose **EC2** when you need full OS-level control.
* Always implement exponential backoff with jitter when handling transient AWS API throttling (`ThrottlingException` / HTTP 429).
