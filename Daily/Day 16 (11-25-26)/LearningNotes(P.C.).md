# Database Fundamentals

Right now, your Lead Management API stores data in `FAKE_LEADS_DB`—a Python list sitting inside your computer's RAM. The moment you restart `uvicorn` or deploy a new version of your app, every single lead created by your users vanishes forever.

A **relational database** (like PostgreSQL) solves this by storing structured data permanently on disk in organized tables. Think of a relational database like a strict, high-speed collection of spreadsheets that can link to one another:

* **Table:** Represents one type of entity (e.g., `leads` or `users`).
* **Row (Record):** Represents one individual item in that table (e.g., Acme Corp).
* **Column (Field):** Represents one specific attribute with a strict data type (e.g., `id` as an integer, `email` as text, `created_at` as a timestamp).
* **Relationship:** Connects rows in one table to rows in another (e.g., linking 50 leads to the specific sales rep in the `users` table who owns them).

---

## Architecture Breakdown (Lead Management API)

In our application, we will design three core relational tables that link together cleanly:

```text
┌───────────────────────────┐       ┌───────────────────────────┐
│          users            │       │           leads           │
├───────────────────────────┤       ├───────────────────────────┤
│ id (PK)           INT     │──┐    │ id (PK)           INT     │
│ email (UNIQUE)    VARCHAR │  │    │ name              VARCHAR │
│ hashed_password   VARCHAR │  └───<│ owner_id (FK)     INT     │
│ full_name         VARCHAR │       │ email             VARCHAR │
│ is_active         BOOLEAN │       │ status            VARCHAR │
└───────────────────────────┘       │ created_at        TIMESTAMP│
                                    └───────────────────────────┘
                                                  │
                                                  ▼
                                    ┌───────────────────────────┐
                                    │        activities         │
                                    ├───────────────────────────┤
                                    │ id (PK)           INT     │
                                    │ lead_id (FK)      INT     │
                                    │ notes             TEXT    │
                                    │ created_at        TIMESTAMP│
                                    └───────────────────────────┘
```

### Key Relational Concepts

* **PK (Primary Key):** A unique ID (`1`, `2`, `3`...) that identifies each row.
* **FK (Foreign Key):** A column that stores the Primary Key of a row in another table, creating a **one-to-many relationship** (one user owns many leads; one lead has many activity notes).
* **Normalization:** Notice we don't repeat the sales rep's name and email inside every single lead row. We store the user once in `users`, and simply reference their `owner_id` in `leads`.
