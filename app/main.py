from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.config import settings

app = FastAPI(
    title=settings.project_name,
    description="A task management system with background processing",
    version="1.0.0",
    openapi_url=f"{settings.api_v1_str}/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.api_v1_str)


@app.get("/")
async def root():
    return {"message": "Task Manager API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
