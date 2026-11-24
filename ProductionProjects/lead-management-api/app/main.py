from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import leads


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic (runs before the app begins accepting requests)
    print("Starting Lead Management API")
    yield
    # Shutdown logic (runs when the server stops)
    print("Shutting Down Lead Management API")


tags_metadata = [
    {
        "name": "Leads",
        "description": "Operations for creating, retrieving, updating, and deleting customer leads.",
    },
]

# Instantiate the FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

# Global middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handlers (will be wired up in Milestone 8)
# app.add_exception_handler(...)

# Versioned API routers
api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(leads.router)

app.include_router(api_v1_router)
