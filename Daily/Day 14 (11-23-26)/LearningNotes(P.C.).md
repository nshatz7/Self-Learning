# Setting up Dependency Injection

**Dependency Injection:** A design pattern where a function declares what resources or logic it needs to work, rather than creating or managing them internally.

---

## Architecture Breakdown for Project 1

Extract reusable request logic into a shared function and inject it into `app/routes/leads.py`:

```text
Incoming Request: GET /api/v1/leads/?skip=0&limit=5
       │
       ▼
1. FastAPI runs pagination_params(skip=0, limit=5)
       │  (Validates limits & returns {"skip": 0, "limit": 5})
       ▼
2. FastAPI injects that dict into get_leads(..., pagination=...)
       │
       ▼
3. get_leads() slices the results and returns JSON
```

---

## What I Did

1. **Updated Imports:** Updated `api/v1/leads.py` to import `Depends` and `Query` from `fastapi`.
2. **Created Reusable `pagination_params` Dependency:** Built a shared function that FastAPI automatically inspects for `skip` and `limit` parameters from the query string:

```python
def pagination_params(
    # Dependency that FastAPI automatically inspects for parameters (skip and limit) and reads from the query string
    skip: int = Query(default=0, ge=0, description="Number of records to skip"),  # "default" and "ge" set up guardrails
    limit: int = Query(default=10, ge=1, le=100, description="Max records to return"),
) -> dict[str, int]:
    return {"skip": skip, "limit": limit}
```

3. **Injected `pagination_params` into `get_leads`:** Used `Depends(pagination_params)` to cleanly handle filtering and pagination:

```python
@router.get("/", response_model=list[LeadResponse], status_code=status.HTTP_200_OK)  # Uses LeadResponse as model; uses list for GET all
def get_leads(
    status: str | None = None,  # Declares optional query parameter; allows status value to be None
    pagination: dict[str, int] = Depends(pagination_params),  # Tells FastAPI to run pagination_params first, then assign its returned dict to pagination
):
    results = FAKE_LEADS_DB

    if status is not None:
        results = [lead for lead in results if lead["status"] == status]  # Filters list in memory if a status query parameter was passed

    skip = pagination["skip"]
    limit = pagination["limit"]
    return results[skip : skip + limit]  # List slicing used for pagination (skip = starting index, skip + limit = stopping index)
```
