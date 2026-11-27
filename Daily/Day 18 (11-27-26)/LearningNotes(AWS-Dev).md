# Course 9: Real-Time Data Streaming (Amazon Kinesis Data Streams & Amazon Data Firehose)

When your system generates continuous streams of events—such as clickstream telemetry, IoT sensor readings, application logs, or financial transactions—standard request/response APIs or simple queues aren't always enough. This course covers real-time data streaming on AWS: capturing and replaying high-throughput event streams with **Amazon Kinesis Data Streams**, and automatically transforming and delivering streaming data to analytics and storage targets with **Amazon Data Firehose**.

---

## 1. Amazon Kinesis Data Streams (KDS): Architecture & Shards

**Amazon Kinesis Data Streams** is a durable, real-time data streaming service where producers push records into a stream and multiple independent consumers read and replay those records. Unlike SQS—where consuming and deleting a message removes it from the queue—Kinesis retains stream records for a configurable retention period (**24 hours by default, up to 365 days**), allowing multiple consumers (or re-running jobs) to read the same data independently.

### Core Building Blocks
* **Data Stream:** A named pipeline composed of one or more shards.
* **Shard:** The fundamental throughput unit of a Kinesis stream. Each shard provides:
  * **Write throughput:** Up to **1 MB/sec** (including partition keys) or **1,000 records/sec**.
  * **Read throughput:** Up to **2 MB/sec** across consumers.
* **Data Record:** Contains a **Partition Key** (string), a **Sequence Number** (unique identifier assigned by Kinesis per shard), and a **Data Blob** (up to **1 MB** payload in standard operations).

### Partition Keys & Ordering
* **Shard Mapping:** Kinesis hashes the Partition Key (using MD5) to map each record to a specific shard.
* **Ordering Guarantee:** Records sharing the same Partition Key always land in the same shard and are read in strict arrival order within that shard.
* **Hot Shard Risk:** Just like DynamoDB partition keys, choosing a low-cardinality partition key (e.g., a single constant value) funnels all writes into one shard, causing `ProvisionedThroughputExceededException` throttling even if other shards sit idle.

### Capacity Modes: On-Demand vs. Provisioned
* **On-Demand Mode:** Automatically manages shard capacity and scales throughput up and down based on traffic volume without manual shard math. Ideal for variable or unpredictable streaming workloads.
* **Provisioned Mode:** You specify the exact number of shards upfront and scale manually via shard splitting (`SplitShard`—doubles shard count for more throughput) or shard merging (`MergeShards`—combines two shards to save cost).

---

## 2. Producers & Consumers: Polling vs. Enhanced Fan-Out

### Producers
* **AWS SDK (`PutRecord` / `PutRecords`):** Send single or batched records directly from your application code or Lambda functions.
* **Kinesis Producer Library (KPL):** A high-throughput producer library that handles automatic retries, batching, aggregation (packing multiple small records into one Kinesis record), and CloudWatch metrics.

### Consumers & Read Models
Consumers read from shards using a **Shard Iterator**, which sets the starting point in the shard:
* `AT_SEQUENCE_NUMBER`
* `AFTER_SEQUENCE_NUMBER`
* `TRIM_HORIZON` (oldest available record)
* `LATEST` (newest records)

| Consumer Pattern | How It Works | Read Throughput Quota | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Shared Throughput (Standard Polling)** | Consumers call `GetRecords` against a shard (up to 5 calls/sec per shard). | **2 MB/sec total** per shard shared across all standard consumers. | 1–2 consumers or Lambda event source mappings with moderate throughput. |
| **Enhanced Fan-Out (EFO)** | Registers a dedicated consumer (`RegisterStreamConsumer`) that receives records pushed over persistent HTTP/2 streams (`SubscribeToShard`). | **Dedicated up to 2 MB/sec** per consumer per shard (up to 20 registered consumers per stream). | Multiple real-time consumers reading simultaneously without contending for shared read bandwidth. |

---

## 3. Amazon Data Firehose: Managed Delivery & Transformation

While Kinesis Data Streams gives you low-level control, replayability, and custom stream consumers, **Amazon Data Firehose** (formerly Kinesis Data Firehose) is a fully managed extract-load-transform (ELT) delivery stream designed to buffer, optionally transform, compress, and deliver streaming data straight to storage and analytics destinations—with **zero shard management**.

### Key Capabilities
* **Automatic Scaling & Buffering:** Scales elastically with ingestion volume and batches incoming records into buffers based on **Buffer Size (MiB)** or **Buffer Interval (seconds)** before writing to the destination. Because of buffering, delivery is **near real-time** rather than sub-second instantaneous.
* **Data Transformation & Format Conversion:**
  * Invoke an **AWS Lambda** function inline to enrich, scrub, or reshape records before delivery.
  * Automatically convert incoming JSON records into columnar analytics formats (**Apache Parquet** or **Apache ORC**) and compress with **GZIP**, **Snappy**, or **ZIP** to shrink S3 storage costs and speed up Amazon Athena queries.
  * **Dynamic partitioning** lets you partition S3 output prefixes by keys inside the data (e.g., `customer_id` or `date`).
* **Supported Destinations:** Amazon S3, Amazon Redshift, Amazon OpenSearch Service, HTTP endpoints, and supported third-party analytics platforms.
* **Error Handling & Backup:** Failed deliveries are retried automatically, and you can configure Firehose to write failed records—or all raw source records—to an S3 backup prefix so no data is lost.

---

## 4. Kinesis Data Streams vs. Amazon Data Firehose

| Feature | Amazon Kinesis Data Streams | Amazon Data Firehose |
| :--- | :--- | :--- |
| **Primary Purpose** | Custom real-time stream ingestion, replay, and multi-consumer processing. | Automated buffering, transformation, and delivery to storage/analytics targets. |
| **Data Retention & Replay** | Retains records for **24 hours to 365 days**; supports multiple independent consumers and replay. | **No retention/replay** once delivered to the destination. |
| **Capacity Management** | On-demand scaling or manual/API shard management (`SplitShard` / `MergeShards`). | Fully automatic scaling; **no shards to manage**. |
| **Delivery Latency** | Sub-second / real-time consumption. | Near real-time (governed by buffer size and buffer interval). |

---

## Key Exam & Best-Practice Takeaways

* **Service Selection:** Choose **Kinesis Data Streams** when you need data replay, multiple independent real-time consumers, or strict per-partition ordering across shards. Choose **Data Firehose** when the goal is simply ingesting, transforming (via Lambda or JSON-to-Parquet), and loading streaming data into S3, Redshift, or OpenSearch with minimal operational overhead.
* **Throughput & Fan-Out:** Each Kinesis shard supports **1 MB/s write** and **2 MB/s read**. Use **Enhanced Fan-Out** when multiple consumers need their own dedicated 2 MB/s read throughput per shard without throttling one another.
* **Firehose Buffering Trade-offs:** In Data Firehose, tune buffer size and buffer interval carefully: larger buffers produce fewer, larger S3 files (better for Athena/Parquet analytics), while smaller intervals deliver data to the destination sooner.
