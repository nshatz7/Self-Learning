# OpenAPI Documentation

**OpenAPI** (formerly known as Swagger) is the industry-standard specification for describing REST APIs in a machine-readable JSON format.

FastAPI automatically inspects every route, path parameter, query parameter, Pydantic request body, `response_model`, and docstring in your codebase to generate a live OpenAPI schema at `/openapi.json`. It then uses that schema to power two built-in interactive documentation interfaces:

* **Swagger UI (`/docs`):** An interactive sandbox where developers can read endpoint specs and send real HTTP requests directly from the browser.
* **ReDoc (`/redoc`):** A clean, three-panel reference manual designed for reading and sharing API contracts.

---

## Architecture Breakdown for Project 1

We enrich our OpenAPI documentation at three levels across the codebase:

| Level | Where It Lives | What It Documents |
| :--- | :--- | :--- |
| **Application Metadata** | `app/main.py` | API title, description, version, and tag descriptions |
| **Route Metadata** | `app/routes/leads.py` | Endpoint summaries, detailed descriptions (via docstrings), and possible error status codes (`404`) |
| **Schema Examples** | `app/schemas/lead.py` | Realistic example JSON payloads shown in `/docs` instead of generic `"string"` placeholders |

---

## Implementation Summary

1. **Added Realistic Schema Examples (`app/schemas/lead.py`):**
   Configured `model_config` with `json_schema_extra` on `LeadCreate` so `/docs` pre-fills realistic CRM data instead of `"string"`:

```python
model_config = ConfigDict(
    json_schema_extra={
        "examples": [
            {
                "name": "Stark Industries",
                "email": "tony@starkindustries.com",
                "status": "new",
            }
        ]
    }
)
```

2. **Enriched Route Metadata (`app/routes/leads.py`):**
   Added `summary`, `responses` (to document `404` errors), and a Markdown docstring to `get_lead_by_id`:

```python
# HTTP method GET (single lead)
@router.get(
    "/{lead_id}",
    response_model=LeadResponse,
    status_code=status.HTTP_200_OK,
    summary="Retrieve a single lead by ID",  # FastAPI uses summary as the short headline next to the URL in /docs, and renders the Markdown docstring inside the expanded endpoint description
    responses={  # Explicitly declaring 404 documents your business logic exceptions for API consumers
        404: {"description": "Lead not found"},
    },
)
def get_lead_by_id(lead_id: int):
    """
    Fetch detailed public information for a specific customer lead:

    - **lead_id**: The unique integer identifier of the lead.
    """
    for lead in FAKE_LEADS_DB:
        if lead["id"] == lead_id:
            return lead

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )
```

3. **Updated Application Metadata (`app/main.py`):**
   Configured the FastAPI app instance with a descriptive summary and tagged metadata.
