# Learning Notes: Setting Up a Path Parameter in FastAPI

## 1. The Concept from the Ground Up

A **path parameter** is a variable embedded directly inside the URL path itself. Instead of hardcoding a separate route for every single record in your database (`/leads/1`, `/leads/2`, `/leads/3`), you define a dynamic placeholder inside curly braces: `/leads/{lead_id}`.

When a client sends a request to `/leads/42`, FastAPI extracts `42` from the URL, converts it to the data type you specified, and passes it directly into your Python function as an argument.

---

## 2. Why Professional Developers Use It

In RESTful API design, URLs represent resources:

* **Collection URL:** `/leads` refers to the entire group of leads.
* **Item URL:** `/leads/{lead_id}` uniquely identifies one specific lead inside that collection.

Using path parameters with strict Python type hints gives you three immediate production advantages:

* **Automatic Data Validation:** If someone requests `/leads/abc` when your function expects `lead_id: int`, FastAPI immediately rejects the request with a `422 Unprocessable Entity` error before your code even runs.
* **Clean Code:** You never have to manually parse strings out of raw URLs.
* **Interactive Documentation:** FastAPI automatically generates input fields for path parameters in your `/docs` Swagger UI.

---

## 3. Architecture Breakdown (Lead Management API)

In `app/routes/leads.py`, we fetch a single lead by its ID and handle the case where that ID doesn't exist:

| URL Requested | Route Matched | Value of `lead_id` | Server Response |
| :--- | :--- | :--- | :--- |
| `GET /leads/` | `@router.get("/")` | N/A | `200 OK` (List of all leads) |
| `GET /leads/1` | `@router.get("/{lead_id}")` | `1` (`int`) | `200 OK` (Lead #1 object) |
| `GET /leads/999` | `@router.get("/{lead_id}")` | `999` (`int`) | `404 Not Found` |
| `GET /leads/hello` | `@router.get("/{lead_id}")` | Rejected | `422 Unprocessable Entity` |

> **Crucial Ordering Rule:** FastAPI evaluates routes from top to bottom. If you ever add a static sub-route like `/leads/stats`, it **must** be placed above `/leads/{lead_id}` in your file—otherwise FastAPI will assume `"stats"` is a `lead_id` and throw a type validation error.

---

## Changelog / What I Did

* Updated `app/routes/leads.py` to include a temporary, mock database.
* Added the `GET /{lead_id}` endpoint to retrieve individual lead records by ID.
