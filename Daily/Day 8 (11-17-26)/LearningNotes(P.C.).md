# Setting Up HTTP Methods


## Core HTTP Methods

| Method | Action | Safe? | Idempotent? |
| :--- | :--- | :---: | :---: |
| **`GET`** | Retrieves data without changing anything. | Yes | Yes |
| **`POST`** | Creates a brand new resource. | No | No |
| **`PUT`** | Completely replaces an existing resource. | No | Yes |
| **`PATCH`** | Partially updates an existing resource (specific fields only). | No | No* |
| **`DELETE`** | Removes an existing resource. | No | Yes |

*\*Note: `PATCH` is not strictly idempotent by specification, though it can be implemented to behave idempotently depending on the operation.*

---

## Method Breakdown

* **`GET`**: Used solely to read or retrieve representations of a resource. It should never modify data on the server.
* **`POST`**: Submits data to the server to create a new subordinate resource. Calling `POST` multiple times typically results in multiple new resources being created.
* **`PUT`**: Replaces the entire target resource with the request payload. If the resource does not exist, it may create one depending on the implementation.
* **`PATCH`**: Applies partial modifications to a resource, updating only the specific fields provided in the request.
* **`DELETE`**: Removes the specified resource from the server.

---

## Key Concepts

### Safety
An HTTP method is considered **safe** if it does not alter the state of the server. Safe methods are read-only operations.
* **Safe:** `GET`
* **Unsafe:** `POST`, `PUT`, `PATCH`, `DELETE`

### Idempotency
An HTTP method is **idempotent** if making the exact same request **1 time** produces the exact same server state as making it **100 times** in a row.
* **Idempotent:** `GET`, `PUT`, `DELETE` *(Note: While subsequent `DELETE` calls might return a `404 Not Found` status code, the state of the server remains unchanged—the resource is still deleted).*
* **Non-Idempotent:** `POST`, `PATCH`
