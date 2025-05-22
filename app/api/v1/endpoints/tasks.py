from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.task import task_crud
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import task_service

router = APIRouter()


@router.post("/", response_model=Task)
async def create_task(
    task_in: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new task"""
    task = await task_crud.create(db=db, obj_in=task_in)
    return task


@router.get("/", response_model=List[Task])
async def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    status: Optional[str] = Query(None),
    title: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    """List tasks with optional filtering"""
    tasks = await task_crud.get_multi(
        db=db, skip=skip, limit=limit, status=status, title=title
    )
    return tasks


@router.get("/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get task by ID"""
    task = await task_crud.get(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=Task)
async def update_task(
    task_id: int,
    task_in: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update task"""
    task = await task_crud.get(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = await task_crud.update(db=db, db_obj=task, obj_in=task_in)
    return task


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete task"""
    task = await task_crud.delete(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@router.post("/{task_id}/process")
async def process_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Start background processing for task"""
    task = await task_crud.get(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Start background processing
    await task_service.start_processing(task_id=task_id)
    
    return {"message": f"Task {task_id} processing started"}
