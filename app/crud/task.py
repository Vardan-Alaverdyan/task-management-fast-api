from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from app.models.task import Task, TaskLog
from app.schemas.task import TaskCreate, TaskUpdate


class TaskCRUD:
    async def get(self, db: AsyncSession, task_id: int) -> Optional[Task]:
        result = await db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    async def get_multi(
        self, 
        db: AsyncSession, 
        skip: int = 0, 
        limit: int = 100,
        status: Optional[str] = None,
        title: Optional[str] = None
    ) -> List[Task]:
        query = select(Task)
        
        if status:
            query = query.where(Task.status == status)
        if title:
            query = query.where(Task.title.ilike(f"%{title}%"))
            
        query = query.offset(skip).limit(limit).order_by(Task.created_at.desc())
        result = await db.execute(query)
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: TaskCreate) -> Task:
        db_obj = Task(**obj_in.dict())
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, db_obj: Task, obj_in: TaskUpdate) -> Task:
        update_data = obj_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, task_id: int) -> Optional[Task]:
        db_obj = await self.get(db, task_id)
        if db_obj:
            await db.delete(db_obj)
            await db.commit()
        return db_obj


task_crud = TaskCRUD()
