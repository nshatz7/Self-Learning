# Setting Up API Versioning

## Overview
**API Versioning** is the practice of embedding a version identifier (most commonly `/api/v1`) directly into the URL path.

---

## Architecture Breakdown (Project 1)

Instead of hardcoding the version prefix into every route file, all `v1` feature routers are grouped under a single parent `APIRouter`:

```text
app (FastAPI)
 └── api_v1_router (prefix="/api/v1")
      ├── leads.router (prefix="/leads")  ──▶ /api/v1/leads
      ├── users.router (prefix="/users")  ──▶ /api/v1/users  (Milestone 6)
      └── auth.router  (prefix="/auth")   ──▶ /api/v1/auth   (Milestone 6)
```

---

## What I Did

### 1. Feature Routes (`app/routes/leads.py`)
* Kept `app/routes/leads.py` unchanged.

### 2. Application Setup (`app/main.py`)
* Created a versioned parent router and attached `leads.router` to it:

```python
# Creates a top-level router whose only job is prefixing everything attached to it with "/api/v1/"
api_v1_router = APIRouter(prefix="/api/v1")

# Nests the "leads" router inside "api_v1_router" (FastAPI automatically concatenates their prefixes)
api_v1_router.include_router(leads.router)

# Mounts the entire v1 router tree onto the main FastAPI application
app.include_router(api_v1_router)
```
