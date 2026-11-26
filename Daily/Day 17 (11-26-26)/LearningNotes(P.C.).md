# SQL Fundamentals

**SQL** (Structured Query Language) is the standard language used to query and modify data in relational databases such as PostgreSQL. Instead of filtering or mutating Python lists in memory, the application sends SQL statements to the database engine, which locates, creates, updates, or deletes rows on disk and returns the result set.

---

## Core CRUD Operations

* **`SELECT`:** Reads rows from a table, commonly narrowed with `WHERE` and ordered with `ORDER BY`.
* **`INSERT`:** Adds new rows into a table (`INSERT INTO ... VALUES ...`).
* **`UPDATE`:** Modifies column values on existing rows that match a `WHERE` filter (`UPDATE ... SET ... WHERE ...`).
* **`DELETE`:** Removes matching rows from a table (`DELETE FROM ... WHERE ...`).

---

## Architecture Breakdown: Lead Management API

For a `leads` table, the four operations map to API actions as follows:

| Operation | SQL Pattern | Purpose in Lead Management API |
| :--- | :--- | :--- |
| **Read** | `SELECT ... FROM leads WHERE ...` | Fetch all leads, filter by status, or look up a single lead by `id` |
| **Create** | `INSERT INTO leads (...) VALUES (...)` | Insert a new lead record into `leads` |
| **Update** | `UPDATE leads SET ... WHERE id = ...` | Change a lead's status or contact/account details |
| **Delete** | `DELETE FROM leads WHERE id = ...` | Remove a lead record by `id` |

> **Best Practice:** Always include a `WHERE` clause on `UPDATE` and `DELETE` statements unless you intend to modify or remove every row in the `leads` table.
