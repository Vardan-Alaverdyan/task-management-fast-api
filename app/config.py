from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://taskuser:taskpassword@localhost:5432/taskmanager"
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "taskmanager"
    database_user: str = "taskuser"
    database_password: str = "taskpassword"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    redis_host: str = "localhost"
    redis_port: int = 6379
    
    # Application
    environment: str = "development"
    debug: bool = True
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # Logging
    log_level: str = "INFO"
    
    # Task settings
    task_timeout: int = 300
    max_retries: int = 3
    
    # Security
    secret_key: str = "your-secret-key-change-in-production"
    
    # API
    api_v1_str: str = "/api/v1"
    project_name: str = "Task Manager API"
    
    class Config:
        env_file = ".env"


settings = Settings()
