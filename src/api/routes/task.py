from fastapi import APIRouter

from src.schemas.task import TaskResponseSchema, TaskCreateSchema, TaskEditSchema, TaskUpdateSchema
from src.services.task_service import TaskService
from src.db.dependencies import DbSessionDep


router = APIRouter(prefix="/task", tags=["Task"])




@router.post("")
async def add_task(db: DbSessionDep, task_data: TaskCreateSchema):
    task_service = TaskService(db)
    await task_service.add_task(task_data)
    return {"msg": "The task has been added"}
    



@router.get("", response_model=list[TaskResponseSchema])
async def get_tasks(db: DbSessionDep):
    task_service = TaskService(db)
    return await task_service.get_task()


@router.get("/{task_id}", response_model=TaskResponseSchema)
async def get_task(db: DbSessionDep, task_id: int):
    task_service = TaskService(db)
    return await task_service.get_task_by_id(task_id)



@router.patch("/{task_id}")
async def edit_task(db: DbSessionDep, task_id: int, task_data: TaskEditSchema):
    task_service = TaskService(db)
    await task_service.update_task(task_id, task_data)
    return {"msg": "Task has been edited"}


@router.put("/{task_id}")
async def update_task(db: DbSessionDep, task_id: int, task_data: TaskUpdateSchema):
    task_service = TaskService(db)
    await task_service.update_task(task_id, task_data)
    return {"msg": "Task has been updated"}


@router.delete("/{task_id}")
async def delete_task(db: DbSessionDep, task_id: int):
    task_service = TaskService(db)
    await task_service.delete_task(task_id)
    return {"msg": "Task has been deleted"}


