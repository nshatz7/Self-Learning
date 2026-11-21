# Course 4: Adding Data to Your API (Amazon DynamoDB)

This course introduces **Amazon DynamoDB**, AWS’s fully managed, serverless NoSQL key-value and document database. Unlike relational databases (SQL) that normalize data across multiple tables and rely on expensive `JOIN` operations, DynamoDB is engineered for single-digit millisecond performance at any scale by modeling data around known application access patterns.

---

## 1. Core DynamoDB Hierarchy & Primary Keys

DynamoDB organizes data into **Tables** -> **Items** (analogous to rows, max size `400 KB`) -> **Attributes** (analogous to columns; schemaless except for the primary key).

Every item in a table must be uniquely identified by its **Primary Key**, which comes in two forms:

1. **Simple Primary Key (Partition Key Only):**
   * Consists of a single attribute (`PK`). DynamoDB hashes this value to determine which physical storage partition holds the item.
   * **Constraint:** Every item in the table must have a unique Partition Key value.
2. **Composite Primary Key (Partition Key + Sort Key):**
   * Consists of a Partition Key (`PK`) and a Sort Key (`SK`).
   * Multiple items can share the same `PK` (forming an *item collection*), provided each has a distinct `SK`.
   * All items with the same `PK` are stored physically together and ordered by their `SK` (UTF-8 string order, numeric order, or binary order), enabling fast range queries (`begins_with`, `between`, `<`, `>`).

### Designing Good Partition Keys (Avoiding Hot Partitions)

* **High Cardinality:** Choose keys with many distinct values (e.g., `USER#123`, `ORDER#987`) so read/write traffic distributes evenly across underlying storage partitions.
* **Anti-pattern:** Using low-cardinality attributes like status (`PENDING`/`COMPLETE`) or date (`2026-11-20`) as a Partition Key forces all active traffic onto a single physical partition, causing hot partition throttling (`ProvisionedThroughputExceededException`).

---

## 2. Secondary Indexes: LSI vs. GSI

When your application needs to query items using attributes other than the base table's primary key, you create a secondary index.

| Feature | Local Secondary Index (LSI) | Global Secondary Index (GSI) |
| :--- | :--- | :--- |
| **Partition Key** | Must be the exact same `PK` as the base table. | Can be any attribute (different `PK` and optional `SK`). |
| **When Created** | Only at table creation time (cannot be added or deleted later). | Can be created, modified, or deleted at any time. |
| **Read Consistency** | Supports both Eventually Consistent and Strongly Consistent reads. | Supports Eventually Consistent reads **ONLY**. |
| **Throughput** | Shares RCU/WCU capacity with the base table. | Has its own independent RCU/WCU capacity. |
| **Partition Size Limit** | Item collection (base table + all LSIs for a `PK`) capped at `10 GB`. | No `10 GB` item collection limit. |

* **Projection Types:** When creating an index, you choose which attributes are copied from the base table:
  * `KEYS_ONLY`: Lowest storage/write cost.
  * `INCLUDE`: Specific attributes.
  * `ALL`: Highest cost, avoids fetching from the base table.

---

## 3. Reading & Writing Data via the SDK (CRUD)

### Query vs. Scan (Critical Performance Rule)

* **Query (Best Practice):** Locates items directly using the Partition Key (and an optional Sort Key condition). Fast, predictable, and consumes capacity proportional only to the items matched.
* **Scan (Avoid in Production):** Reads every single item in the entire table and applies a `FilterExpression` *after* reading the data. Applying a filter does not reduce Read Capacity Units (RCUs) consumed—you still pay to read the entire table.

### Read Consistency Models

* **Eventually Consistent Reads (Default):** Returns data in milliseconds, though a write completed milliseconds earlier might not be reflected yet. Costs `0.5 RCU` per `4 KB` item.
* **Strongly Consistent Reads (`ConsistentRead=True`):** Guarantees returning the most up-to-date data after all prior successful writes. Costs `1 RCU` per `4 KB` item (double the cost).

### Boto3 SDK Example (CRUD Operations)

Using `boto3.resource("dynamodb")` automatically serializes native Python types into DynamoDB JSON types (unlike the low-level `boto3.client`, which requires `{"S": "value"}` wrappers):

```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("OrdersTable")

# 1. Create / Replace Item (PutItem)
table.put_item(
    Item={
        "PK": "USER#101",
        "SK": "ORDER#2026-11-20#001",
        "status": "CONFIRMED",
        "total": 89
    },
    # Conditional write: prevent overwriting an existing order
    ConditionExpression="attribute_not_exists(PK)"
)

# 2. Get Single Item (GetItem - requires full Primary Key)
response = table.get_item(
    Key={"PK": "USER#101", "SK": "ORDER#2026-11-20#001"}
)
item = response.get("Item")

# 3. Query Item Collection (All November 2026 orders for USER#101)
orders = table.query(
    KeyConditionExpression=Key("PK").eq("USER#101") & Key("SK").begins_with("ORDER#2026-11")
)

# 4. Atomic Update (UpdateItem)
table.update_item(
    Key={"PK": "USER#101", "SK": "ORDER#2026-11-20#001"},
    UpdateExpression="SET #s = :new_status",
    ExpressionAttributeNames={"#s": "status"},  # 'status' is a reserved keyword in DynamoDB
    ExpressionAttributeValues={":new_status": "SHIPPED"}
)
```

---

## 4. Capacity Modes, TTL, & DynamoDB Streams

* **Capacity Modes:**
  * **On-Demand Mode:** Pay-per-request pricing. Scales automatically with zero capacity planning—ideal for unpredictable, spiky serverless workloads.
  * **Provisioned Mode:** You specify exact RCUs (`1 RCU` = one `4 KB` strongly consistent read/sec or two eventually consistent reads/sec) and WCUs (`1 WCU` = one `1 KB` write/sec). Cheaper for steady, predictable traffic; pairs with Auto Scaling.
* **Time to Live (TTL):** Designate a Unix epoch timestamp attribute (e.g., `expires_at`). DynamoDB automatically deletes expired items in the background at zero WCU cost (usually within 48 hours)—ideal for session tokens or temporary logs.
* **DynamoDB Streams:** Captures a time-ordered sequence of item-level modifications (`INSERT`, `MODIFY`, `REMOVE`) for 24 hours. Often wired directly to an AWS Lambda trigger to react asynchronously to database changes (e.g., sending an email when a new user row is inserted).

---

## Key Exam & Best-Practice Takeaways

* Never use `Scan` for routine API endpoints; redesign your keys or add a GSI so every access pattern uses `GetItem` or `Query`.
* Primary Key attributes (`PK` and `SK`) cannot be updated in place—modifying a key requires deleting the old item and inserting a new one (ideally inside a `TransactWriteItems` call).
* Use **Conditional Writes** (`ConditionExpression`) for optimistic locking and preventing duplicate writes without needing heavy distributed transactions.
* DynamoDB items have a strict `400 KB` maximum size limit; store large files/images in Amazon S3 and save only the S3 object URL/key in DynamoDB.
