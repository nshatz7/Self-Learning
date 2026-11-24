# Course 6: Scaling with Data Storage (Amazon S3 & Amazon ElastiCache)

As applications scale, storing large binary files in databases or repeatedly querying databases for identical read-heavy data creates severe latency bottlenecks and high costs. This course covers two foundational storage patterns: offloading unstructured objects to **Amazon S3** and accelerating sub-millisecond reads using **Amazon ElastiCache**.

---

## 1. Amazon S3 for Developers

**Amazon Simple Storage Service (S3)** is an infinitely scalable object store designed for **99.999999999% (11 nines)** of durability. Objects (up to **5 TB** each) live inside globally uniquely named buckets and are identified by a key (path) and optional metadata.

### Presigned URLs (Secure Direct-to-S3 Uploads & Downloads)

Routing large file uploads or downloads through your backend API Gateway or Lambda function wastes compute memory, triggers payload limits (API Gateway caps payloads at **10 MB**, Lambda synchronous payloads at **6 MB**), and adds latency.

Instead, developers use **Presigned URLs**:

1. The client authenticates with your backend API and requests permission to upload/download a file.
2. Your backend Lambda function uses the AWS SDK (and its IAM Execution Role) to generate a cryptographically signed, temporary URL with an expiration timer (e.g., 5 minutes).
3. The client uses that URL to upload (`PUT`) or download (`GET`) the object directly with S3, completely bypassing your backend servers.

```python
import boto3

s3_client = boto3.client("s3")

# Generate a temporary URL valid for 300 seconds (5 minutes)
presigned_url = s3_client.generate_presigned_url(
    ClientMethod="put_object",
    Params={
        "Bucket": "my-app-uploads-prod",
        "Key": "avatars/user-101.png",
        "ContentType": "image/png"
    },
    ExpiresIn=300
)
```

> **Exam Tip:** A presigned URL inherits the exact permissions of the IAM identity that generated it. If an IAM role lacks `s3:PutObject` permission, the generated presigned URL will fail with `403 AccessDenied` even if the URL hasn't expired.

### Multipart Uploads & Performance Optimization

* **Multipart Upload:** Recommended for files larger than **100 MB** and mandatory for files over **5 GB**. Splits the object into independent chunks uploaded in parallel—improving throughput and allowing failed parts to be retried individually without restarting the entire upload.
* **Transfer Acceleration:** Routes client uploads to the nearest Amazon CloudFront Edge Location, then forwards traffic over AWS's private backbone network to the target S3 bucket for faster long-distance transfers.
* **Byte-Range Fetches:** Allows applications to request specific byte ranges of an object in parallel (speeding up downloads) or read only the header of a large file.

### S3 Storage Classes & Lifecycle Policies

Lifecycle rules automate cost optimization by transitioning aging objects to cheaper storage tiers or expiring temporary data:

| Storage Class | Retrieval Latency | Minimum Storage Duration | Best Use Case |
| :--- | :--- | :--- | :--- |
| **S3 Standard** | Milliseconds | None | Frequently accessed active data (websites, mobile assets). |
| **S3 Intelligent-Tiering** | Milliseconds | None (small monitoring fee) | Unknown or unpredictable access patterns; automatically moves objects between tiers. |
| **S3 Standard-IA (Infrequent Access)** | Milliseconds | 30 days | Backups or older data accessed less than once a month (per-GB retrieval fee applies). |
| **S3 Glacier Instant Retrieval** | Milliseconds | 90 days | Archival data requiring immediate access once a quarter (e.g., medical imaging). |
| **S3 Glacier Flexible Retrieval** | Minutes to hours | 90 days | Archive backups where 1–5 min (Expedited) or 3–5 hr (Standard) retrieval is acceptable. |
| **S3 Glacier Deep Archive** | 12 to 48 hours | 180 days | Lowest-cost long-term compliance retention (7–10+ years). |

---

## 2. In-Memory Caching with Amazon ElastiCache

**Amazon ElastiCache** is a managed in-memory data store supporting **Valkey**, **Redis OSS**, and **Memcached**. It offloads repetitive read queries from primary databases (RDS or DynamoDB) and serves responses in sub-millisecond latency.

### Engine Comparison: Valkey / Redis vs. Memcached

* **Valkey & Redis OSS:** Rich data structures (Strings, Hashes, Lists, Sets, Sorted Sets for real-time leaderboards), Multi-AZ automatic failover with read replicas, persistence (snapshots/AOF), and pub/sub messaging. Default choice for most production workloads.
* **Memcached:** Simple key-value object cache, multithreaded architecture (scales vertically across CPU cores), no persistence, no replication/failover. Best for simple, volatile, purely horizontal caches.

### Core Caching Strategies

#### 1. Lazy Loading (Cache-Aside)
The application checks the cache first before querying the database:
1. **Cache Hit:** Data exists in ElastiCache $\rightarrow$ return immediately.
2. **Cache Miss:** Data is absent $\rightarrow$ query the database, write the result into ElastiCache with a TTL, and return it to the user.

* **Pros:** Only requested data is cached (saves RAM); if the cache node fails, the app degrades gracefully by falling back to the database.
* **Cons:** Cache miss penalty (3 network hops on first read) and potential stale data until the TTL expires.

#### 2. Write-Through
Whenever the application writes or updates data in the database, it immediately updates the cache in the same operation:

* **Pros:** Cache data is never stale; virtually eliminates read cache misses.
* **Cons:** Adds latency to every write operation (two writes per update) and fills cache memory with data that may never be read.

### TTLs & Eviction Policies

* **Time to Live (TTL):** Always attach a TTL (e.g., `SETEX key 300 value`) to prevent stale data from living forever.
* **Eviction Policies:** When cache memory (`maxmemory`) fills up, ElastiCache evicts keys based on your configured policy—most commonly `allkeys-lru` (evicts Least Recently Used keys across the entire cache) or `volatile-lru` (evicts LRU keys only among keys with an expiration set).

> **Note:** If you specifically need microsecond read caching strictly in front of Amazon DynamoDB without rewriting application query logic, AWS also offers **DynamoDB Accelerator (DAX)**, an API-compatible write-through cache cluster.

---

## Key Exam & Best-Practice Takeaways

* **Use S3 Presigned URLs** whenever clients need to upload or download large files directly without passing payloads through API Gateway or Lambda.
* **Use Multipart Upload** for files `> 100 MB` (required `> 5 GB`) to enable parallel chunk uploads and resilient retries.
* **Combine Lazy Loading + TTL** as your default caching pattern; add **Write-Through** only for data that must remain immediately consistent on read.
* **Use Redis / Valkey Sorted Sets** (`ZADD`, `ZREVRANGE`) when an exam scenario asks for a real-time gaming leaderboard.
