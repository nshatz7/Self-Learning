# Setting up Request Bodies

## Overview
* **Request Body:** A JSON payload attached to the body of an HTTP `POST`, `PUT`, or `PATCH` request.
* **Use Case:** Used when a client needs to send complex, secured data to the server (e.g., creating a new lead with a name, email, company, status, etc.).
  * *Why not use the URL?* Putting complex data into a URL makes it messy, unsecure, and prone to hitting URL length limits.

### Defining the Request Body Shape
* To define the exact shape of a request body, use a **Pydantic `BaseModel`**.
* When a parameter in your route function is typed as a Pydantic model (rather than basic types like `int` or `str`), FastAPI automatically reads from the JSON request body instead of the URL path or query string.

---

## Architecture Breakdown (Project 1)

* `app/schemas/lead.py`: Defines the data shapes (contracts) for incoming and outgoing lead data.
* `app/routes/leads.py`: Imports schemas and uses them to validate incoming request bodies.

| Endpoint | Request Body Schema | Required Fields | Optional Fields (with defaults) |
| :--- | :--- | :--- | :--- |
| `POST /leads/` | `LeadCreate` | `name` (`str`), `email` (`str`) | `status` (`str = "new"`) |
| `PATCH /leads/{lead_id}` | `LeadUpdate` | None | `name`, `email`, `status` (all default to `None`) |

---

## Implementation Details

### 1. Define Request Body Models (`app/schemas/lead.py`)
Created the Pydantic models to enforce data validation rules.

```python
from pydantic import BaseModel


# Inherits from Pydantic's BaseModel.
# 'name' and 'email' have no default values, making them required (unlike 'status').
class LeadCreate(BaseModel):
    name: str
    email: str
    status: str = "new"


class LeadUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    status: str | None = None
```

### 2. Update Route Handlers (`app/routes/leads.py`)
* Imported `LeadCreate` and `LeadUpdate` from `app/schemas/lead.py`.
* Replaced generic `dict` types on `POST`, `PUT`, and `PATCH` routes with the new Pydantic schemas.
* Added the `exclude_unset=True` "secret weapon" to `PATCH` requests to prevent partial updates from overwriting existing data with `None`.

```python
from app.schemas.lead import LeadCreate, LeadUpdate

# ...

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lead(lead_in: LeadCreate):
    # FastAPI recognizes LeadCreate as a BaseModel, automatically parsing 
    # and validating the incoming JSON request body.
    new_lead = {
        "id": len(FAKE_LEADS_DB) + 1,
        # Converts the validated Pydantic object into a standard Python dict for unpacking
        **lead_in.model_dump(),
    }
    FAKE_LEADS_DB.append(new_lead)
    return new_lead

# ...

@router.patch("/{lead_id}", status_code=status.HTTP_200_OK)
def update_lead(lead_id: int, lead_in: LeadUpdate):
    for lead in FAKE_LEADS_DB:
        if lead["id"] == lead_id:
            # Secret weapon for PATCH requests: If the client only sends {"status": "qualified"}, 
            # this strips out 'name' and 'email' instead of overwriting them with None.
            updates = lead_in.model_dump(exclude_unset=True)
            lead.update(updates)
            return lead

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )
```
