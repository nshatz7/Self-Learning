# FastAPI Fundamentals: Coffee Shop Order API

To teach you FastAPI from the ground up without spoiling your Lead Management API architecture, we will use a Coffee Shop Order API as our neutral example domain. This lets you see the exact mechanics in action while leaving you to design and write the Lead Management implementation yourself.

## App Instance, Decorators, and Route Handlers

Every FastAPI application starts by instantiating the `FastAPI` class, which acts as the central registry for your web server. To expose endpoints, you pair decorators with route handlers.

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Coffee Shop API")

# Pydantic defines the shape and validation rules for incoming JSON
class OrderCreate(BaseModel):
    drink: str
    size: str = "medium"
    shots: int = 1

# 1. Decorator: Binds HTTP POST + "/orders/" to the function below
@app.post("/orders/", status_code=status.HTTP_201_CREATED)
# 2. Route Handler: Runs when a matching request arrives
async def place_order(order: OrderCreate):
    # `order` is already validated and converted into a Python object
    return {"ticket_number": 42, "item": order.drink, "size": order.size}
```

* **Decorators (`@app.post(...)`):** A Python wrapper that registers a URL path and HTTP method (`GET`, `POST`, `PUT`, `DELETE`) into FastAPI's routing table, along with metadata like the default HTTP response status code.
* **Route Handlers (`async def place_order(...)`):** The function containing your endpoint logic. FastAPI inspects the type hints in the function signature (`order: OrderCreate`) to automatically parse incoming JSON, validate types, and return a `422 Unprocessable Entity` error if the client sends bad data.

## Scaling Structure: APIRouter

As an API grows, putting every endpoint in `main.py` creates a tangled monolith. `APIRouter` works like a mini-FastAPI instance that lets you split endpoints by domain into separate files and plug them into the main app.

**`routers/menu.py`**

```python
from fastapi import APIRouter, HTTPException

# All routes here automatically start with "/menu" and group under "Menu" in docs
router = APIRouter(prefix="/menu", tags=["Menu"])

@router.get("/{item_id}")
async def get_menu_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Drink not on menu")
    return {"id": 1, "name": "Cortado", "price": 4.25}
```

**`main.py`**

```python
from fastapi import FastAPI
from routers import menu

app = FastAPI(title="Coffee Shop API")

# Mount the router onto the main application
app.include_router(menu.router)
```

Because of `prefix="/menu"`, `get_menu_item` is exposed at `GET /menu/{item_id}` while keeping `main.py` clean.

## Dependency Injection (Depends)

Dependency Injection lets a route handler declare external resources or checks it needs—such as a database connection, pagination settings, or user authentication—without duplicating setup and teardown logic inside every route.

```python
from typing import Annotated
from fastapi import Depends, Header, HTTPException

# Dependency 1: Resource setup and automatic cleanup using `yield`
async def get_register_connection():
    conn = {"register_id": "REG-01", "status": "open"}
    try:
        yield conn  # Hands `conn` to the route handler
    finally:
        conn["status"] = "closed"  # Runs automatically after the response is sent

# Dependency 2: Auth check reading a request header
async def verify_barista(x_badge_id: Annotated[str, Header()]):
    if x_badge_id != "barista-99":
        raise HTTPException(status_code=401, detail="Invalid Barista Badge")
    return {"barista": "Sam"}

# Route declares both dependencies in its signature
@router.post("/brew")
async def brew_drink(
    register: Annotated[dict, Depends(get_register_connection)],
    staff: Annotated[dict, Depends(verify_barista)],
):
    return {"brewed_by": staff["barista"], "register": register["register_id"]}
```

FastAPI resolves the dependency tree before running `brew_drink`. If `verify_barista` raises a `401`, the route handler never executes.

## Middleware

While dependencies operate on specific routes and understand FastAPI types, middleware wraps the entire application at the raw HTTP level. Every request passes through middleware on the way in, and every response passes back through on the way out.

```python
import time
from fastapi import Request

@app.middleware("http")
async def measure_prep_time(request: Request, call_next):
    # 1. Runs BEFORE routing or route handlers
    start = time.perf_counter()

    # 2. Forwards the request down to the matching router/endpoint
    response = await call_next(request)

    # 3. Runs AFTER the route handler creates a response
    duration = time.perf_counter() - start
    response.headers["X-Prep-Time"] = f"{duration:.4f}s"
    return response
```

Middleware is ideal for cross-cutting concerns that apply universally across all endpoints—such as request timing, logging, CORS headers, or attaching request IDs.

## Request Lifecycle

When a customer app sends `POST /orders/` with headers and a JSON body, FastAPI processes it in a strict order:

1. **ASGI Server (Uvicorn):** Receives raw network bytes and translates them into a Python ASGI request object.
2. **Inbound Middleware:** Executes top-to-bottom (e.g., starts timers, checks CORS).
3. **Routing:** Matches the HTTP method (`POST`) and path (`/orders/`) across `app` and any mounted `APIRouters`.
4. **Dependency Resolution:** Runs `Depends()` functions (e.g., opens connections, verifies auth tokens). Short-circuits immediately if an exception like `401` is raised.
5. **Data Validation:** Pydantic parses path parameters, query parameters, headers, and the JSON body against your type hints. Short-circuits with `422` if validation fails.
6. **Route Handler Execution:** Runs your `async def` or `def` endpoint function.
7. **Response Serialization:** Converts the returned Python dictionary or model into JSON (filtering fields if `response_model` is set).
8. **Dependency Teardown:** Executes the `finally` blocks of any `yield` dependencies.
9. **Outbound Middleware:** Executes bottom-to-top (e.g., injects `X-Prep-Time` headers) before Uvicorn sends the HTTP response back to the client.
