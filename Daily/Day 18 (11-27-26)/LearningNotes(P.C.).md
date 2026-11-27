# Project 1: Database Engineering (PostgreSQL Setup)

## 1. The Concept from the Ground Up

**PostgreSQL** (often called "Postgres"): a powerhouse, open-source relational database management system. When you install PostgreSQL on your machine, you are running a database server (a background daemon) that listens for connections—typically on **port `5432`**—and manages databases, roles/users, tables, and data files on disk.

* Unlike SQLite (which stores an entire database inside a single local file), PostgreSQL runs as a dedicated **client-server service**. Your FastAPI application acts as a client that opens a network/socket connection to the PostgreSQL server and sends SQL commands over it.

---

## 2. Why Professional Developers Use It

Professional backend teams overwhelmingly choose PostgreSQL for production web applications because:

* **Rock-Solid Reliability & ACID Compliance:** It handles transactions safely and recovers cleanly from crashes.
* **Rich Data Types:** Beyond standard integers, text, and timestamps, PostgreSQL natively supports `JSONB`, `UUID`s, arrays, full-text search, and strict constraints.
* **Production Parity:** Running PostgreSQL locally during development mirrors what you'll run in Docker (Milestone 9) and on AWS RDS (Milestone 11), catching Postgres-specific SQL behavior early instead of discovering surprises after deployment.

---

## 3. Architecture Breakdown (Lead Management API)

On your Mac (or inside Docker later), a single PostgreSQL server instance can host multiple isolated databases, protected by credentials stored in your environment configuration (`app/config.py` / `.env`):

```text
┌─────────────────────────────────────────────┐
│        Your Python / FastAPI Process        │
│   Reads DATABASE_URL from .env / config.py  │
└──────────────────────┬──────────────────────┘
                       │ TCP Port 5432
                       ▼
┌─────────────────────────────────────────────┐
│            PostgreSQL Server                │
│  ┌───────────────────────────────────────┐  │
│  │  Database: lead_management_dev        │  │
│  │   ├── Table: users                    │  │
│  │   ├── Table: leads                    │  │
│  │   └── Table: activities               │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## 4. Terminal Commands (macOS)

On macOS, the cleanest local setup is Homebrew (or Docker Desktop if you already use Docker). Here are the commands to install, start, and create a dedicated database for our project:

```bash
# 1. Install PostgreSQL via Homebrew (if not already installed)
brew install postgresql@16

# 2. Start PostgreSQL as a background service
brew services start postgresql@16

# 3. Verify the server is running
pg_isready

# 4. Open the interactive Postgres shell (psql) using your macOS user
psql postgres
```

Once inside the `psql` prompt (`postgres=#`), create a dedicated database for the project and list databases to verify:

```sql
-- Create a dedicated database for development
CREATE DATABASE lead_management_dev;

-- List databases to confirm it exists
\l

-- Exit psql
\q
```

> **Tip:** If connecting to database directly is need later, run: `psql lead_management_dev`.

