from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = 1


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None


class TaskInDB(TaskBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Task(TaskInDB):
    pass


class TaskLogBase(BaseModel):
    task_id: int
    status: str
    message: Optional[str] = None


class TaskLogCreate(TaskLogBase):
    pass


class TaskLogInDB(TaskLogBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TaskLog(TaskLogInDB):
    pass
