from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import leads
from app.core.exceptions import (
    #exception classes and handlers
)



@asynccontextmanager #decorator
async def lifespan(app: FastAPI): #defining asynccontextmanager function names "lifespan" that accepts the app instance
    #startup logic (anything before "yield")
    print("Starting Lead Management API")

    yield

    #shut-down logic (anything after "yield")
    print("Shutting Down Lead Management API")


#instantiating the FastAPI application
app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.VERSION,
    description = settings.DESCRIPTION,
    lifespan = lifespan
)

#global middleware
app.add_middleware(
    CORSMiddleware, #the middleware class itself (without parenthases, FastAPI instantiates it internally)
    allow_origins=settings.CORS_ORIGINS, #pulls list of trusted frontend URLs so browser knows which domains are permitted to make requests to API
    allow_credentials=True, #Allows browsers to send cookies or AUTHORIZATION headers
    allow_methods=["*"], #Permits all HTTP methods
    allow_headers=["*"], #Permits all HTTP request headers
)

#gloabl exception handlers
app.add_exception_handler(#exceptions)
    
#Modular routers
app.include_router(leads.router)


    



    

    





