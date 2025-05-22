import asyncio
from app.database import AsyncSessionLocal
from app.crud.task import task_crud


async def process_task_background(task_id: int):
    """Background task processing"""
    print(f"Starting to process task {task_id}")
    
    # Simulate long-running task
    await asyncio.sleep(5)
    
    # Update task status to completed
    async with AsyncSessionLocal() as db:
        task = await task_crud.get(db=db, task_id=task_id)
        if task:
            from app.schemas.task import TaskUpdate
            await task_crud.update(
                db=db, 
                db_obj=task, 
                obj_in=TaskUpdate(status="completed")
            )
    
    print(f"Task {task_id} processing completed")
