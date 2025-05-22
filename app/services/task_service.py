import asyncio
from typing import Optional
from app.background.tasks import process_task_background


class TaskService:
    async def start_processing(self, task_id: int) -> None:
        """Start background processing for a task"""
        # This would typically add task to a queue (Redis/Celery)
        # For now, we'll simulate with asyncio
        asyncio.create_task(process_task_background(task_id))


task_service = TaskService()
