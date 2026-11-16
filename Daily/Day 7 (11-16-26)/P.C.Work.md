# FastAPI Application Entry Point Setup

## 1. Building Blocks are Imported
* The `FastAPI` class is imported by me from the `fastapi` library.
* My `settings` object is imported from `app/config.py` so that access to my environment variables (such as project name, version, and CORS origins) is granted to the entry point.
* The `APIRouter` objects created inside my `app/routes/` modules (e.g., `leads`, `users`, `auth`) are imported by me.

## 2. The Lifespan Manager is Defined *(Optional at first, essential for production)*
* An `asynccontextmanager` function named `lifespan` that accepts the `app` instance is created by me.
* Anything placed by me before the `yield` keyword is executed once when the server is booted up (e.g., logging that the API is being started).
* Anything placed by me after the `yield` keyword is executed once when the server is shut down (e.g., database connections are closed).

## 3. The FastAPI Application is Instantiated
* A module-level variable named `app` is created by me via calling `FastAPI(...)`.
* My metadata arguments (`title`, `version`, `description`) are passed in dynamically from my `config.py` settings, and my `lifespan` function is attached if it was created by me.

## 4. Global Middleware is Attached
* `app.add_middleware(...)` is called by me directly below my `app` instantiation.
* `CORSMiddleware` is registered first so that communication with my API is safely enabled for future frontend clients (or Swagger UI), while the allowed origins list is pulled from my settings rather than being hardcoded.

## 5. Global Exception Handlers are Registered
* Any custom exception handlers from `app/core/exceptions.py` are attached by me to my `app` instance using `app.add_exception_handler(...)` so that clean JSON is returned instead of raw stack traces when unexpected errors occur.

## 6. Modular Routers are Mounted
* `app.include_router(...)` is used by me to plug each imported router (`auth`, `users`, `leads`) into the main application.
* The `prefix="/api/v1"` argument is passed here (or a master v1 router is attached) so that my API versioning is automatically inherited by every endpoint.
