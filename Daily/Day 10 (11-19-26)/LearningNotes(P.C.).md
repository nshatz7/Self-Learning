# Setting up Query Parameters

**Query Parameter:** A key-value pair appended to the end of a URL after a question mark (`?`). If there are multiple query parameters, they are separated by an ampersand (`&`).

---

## Architecture Breakdown for Project 1

| URL Requested | `status` | `skip` | `limit` | Result |
| :--- | :--- | :--- | :--- | :--- |
| `GET /leads/` | `None` | `0` | `10` | Returns up to the first 10 leads |
| `GET /leads/?status=new` | `"new"` | `0` | `10` | Returns only leads with `"status": "new"` |
| `GET /leads/?skip=1&limit=1` | `None` | `1` | `1` | Skips the 1st lead and returns the 2nd |
| `GET /leads/?status=new&limit=5` | `"new"` | `0` | `5` | Returns up to 5 `"new"` leads |

---

## What I Did

* Updated `FAKE_LEADS_DB`
* Updated the `get_leads` function:

```python
def get_leads(
    # Declares optional query parameter; lets status value be "None"
    status: str | None = None,
    # Declares two integer query parameters with default values. 
    # If a user sends "?limit=abc", FastAPI automatically validates the type 
    # and returns a 422 error ("abc" can't be converted to an integer).
    skip: int = 0,
    limit: int = 10,
):
    results = FAKE_LEADS_DB
    
    # Filters list in memory if a "status" query parameter was passed
    if status is not None:
        results = [lead for lead in results if lead["status"] == status]
        
    # List slicing used for pagination (skip = starting index, skip + limit = stopping index)
    return results[skip : skip + limit]
```
