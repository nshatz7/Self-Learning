Python Backend Architecture & Project Standards
===============================================

A reference guide for project isolation, data modeling, REST API conventions, service registration, and layered clean architecture.

---

Table of Contents
-----------------
1. Virtual Environments & Isolation
2. Packages & Python Modules
3. Models, Schemas & Pydantic Validation
4. REST API Endpoint Design
5. Service Directory Architecture
6. Separation of Concerns & Layered Architecture
7. Modern Configuration & Tooling

---

1. Virtual Environments & Isolation
-----------------------------------

Isolating dependencies ensures deterministic behavior, avoids system-level package conflicts, and enables reproducible builds across developer workstations and CI/CD pipelines.

CLI Environment Setup
---------------------

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Parameter Breakdown:
* `python3`: Invokes the target Python interpreter.
* `-m`: Runs a library module as a script.
* `venv`: Python built-in virtual environment manager module.
* `.venv`: The local destination directory for installed binaries and site-packages.
* `source .venv/bin/activate`: Modifies shell environment variables (`PATH`, `VIRTUAL_ENV`) to prioritize local virtual environment executables.

Professional Standards
----------------------
* **Controlled Dependencies:** Pin specific versions to prevent breaking changes across updates.
* **Reproducibility:** Every team member and pipeline should recreate the identical environment via configuration files.
* **Explicit Documentation:** Document every dependency and minimum Python version requirement.
* **Git Hygiene:** Never commit `.venv/` to source control. Always add `.venv/` to `.gitignore`.

---

2. Packages & Python Modules
----------------------------

An `__init__.py` file designates a directory as a regular Python package, allowing structured imports across directories.

```bash
touch app/__init__.py
```

* **Purpose:** Enables sub-module discovery and modular code imports (e.g., `from app.services import lead_service`).
* **Namespace vs Package:** In Python 3.3+, directories without `__init__.py` function as implicit namespace packages, but standard packages requiring explicit initialization, package-level variables, or export control via `__all__` rely on `__init__.py`.

---

3. Models, Schemas & Pydantic Validation
----------------------------------------

Modern backend engineering distinguishes between how data is stored in the database versus how data is accepted and validated over the network.

Core Distinction: Schema vs Model
---------------------------------

| Concept | Primary Question | Primary Responsibility | Common Technologies |
| :--- | :--- | :--- | :--- |
| **Schema** | Is this data acceptable? | Payload validation, data parsing, serialization, contract enforcement | Pydantic, Marshmallow |
| **Model** | How should this data be stored? | Database table mapping, record associations, transaction persistence | SQLAlchemy, Tortoise, SQLModel |

Data Modeling (ORM)
-------------------

Object-Relational Mapping (ORM) maps database tables to application classes and row records to class instances:

```python
"""Database Entity Model (ORM)"""
class Lead:
    id: int
    first_name: str
    email: str
```

Payload Validation with Pydantic
--------------------------------

Pydantic verifies types at runtime and rejects malformed payloads before business logic executes:

```python
"""Request Validation Schema"""
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    first_name: str
    email: EmailStr
```

---

4. REST API Endpoint Design
---------------------------

An API route acts as the communication contract between external clients and backend systems. REST conventions map HTTP methods to resource actions:

| HTTP Method | Endpoint URI | Intent / Action | Typical Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/leads` | Retrieve collection of all leads | 200 OK |
| `GET` | `/api/v1/leads/1` | Retrieve single lead by unique identifier | 200 OK / 404 Not Found |
| `POST` | `/api/v1/leads` | Create a new lead record | 201 Created |
| `PATCH` | `/api/v1/leads/1` | Partially update attributes of an existing lead | 200 OK / 400 Bad Request |
| `DELETE` | `/api/v1/leads/1` | Remove a lead record | 204 No Content |

---

5. Service Directory Architecture
---------------------------------

A Service Directory is a centralized registry where operational services, endpoints, instances, and routing metadata are published and resolved.

Core Lifecycle Phases
---------------------

1. **Service Registration:** When a service instance boots up, it broadcasts its unique identifier, network IP/port, protocol, and operational metadata to the central registry.
2. **Health Checking & Heartbeats:** Periodic health checks verify instance availability. If heartbeats fail or timeout thresholds expire, the directory deregisters the instance to halt routing traffic to dead nodes.
3. **Service Discovery & Lookup:** Upstream consumers query the directory by service name to obtain an active list of healthy endpoints for load-balanced execution.

---

6. Separation of Concerns & Layered Architecture
------------------------------------------------

Clean architecture decouples transport layers, business domains, and persistence engines so each can evolve independently.

Architecture Flow
-----------------

```text
[HTTP Client / CLI / Worker]
             │
             ▼
┌──────────────────────────────────────────────┐
│  Presentation Layer (api/, cli/)             │
│  - FastAPI endpoints, CLI commands           │
│  - Request parsing & Pydantic validation     │
│  - Response status serialization             │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Domain / Service Layer (services/, domain/) │
│  - Pure business rules & orchestration       │
│  - Zero framework dependencies               │
│  - Transport-agnostic logic                  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Data / Infrastructure Layer (repos/, db/)   │
│  - SQLAlchemy models, database drivers       │
│  - Repository Pattern implementation         │
│  - External 3rd party APIs (Stripe, Sendgrid)│
└──────────────────────────────────────────────┘
```

Layer Responsibilities
----------------------

* **Presentation Layer (`api/`, `cli/`):**
  Handles protocol conversions (HTTP status codes, CLI flags). Validates request bodies against schemas and invokes domain services. Contains zero SQL queries or raw database interactions.
* **Domain / Service Layer (`services/`, `domain/`):**
  Encapsulates core business rules (e.g., verifying subscription standing prior to order placement). Completely decoupled from web frameworks (FastAPI) and databases (SQLAlchemy). Runs uniformly whether invoked by an HTTP handler, a CLI task, or a background worker.
* **Data / Infrastructure Layer (`repositories/`, `models/`, `integrations/`):**
  Manages external connections (PostgreSQL, Redis, third-party SDKs). Employs the **Repository Pattern** so domain services request data objects without concern for the underlying storage mechanism.

---

7. Modern Configuration & Tooling
---------------------------------

Modern Python dependency and packaging standards have consolidated fragmented legacy configuration files into a centralized declaration format:

```text
Legacy Configuration                   Modern Standard
---------------------                  ---------------
setup.py                               pyproject.toml (PEP 518 / PEP 621)
setup.cfg                              (Single file for build backend,
requirements.txt                       dependencies, tool configs:
requirements-dev.txt                   ruff, black, mypy, pytest)
```

Best Practices
--------------
* Consolidate dependencies, build metadata, and linter settings within `pyproject.toml`.
* Use lockfiles (e.g., via Poetry, `uv`, or PDM) to guarantee identical dependency resolution across production environments.
    
