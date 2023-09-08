from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from database import get_all_tasks, get_one_task_id, create_task, update_task, delete_task, get_one_task_title
from errors import processing_failure
from models import TaskRead, TaskWrite, UpdateTask

task = APIRouter()


# Retorno Raiz
@task.get('/')
def welcome():
    return {'message': 'Bem-vindo ao FastAPI'}


# Retorna todas as tasks
@task.get('/api/tasks')
async def get_all():
    tasks = await get_all_tasks()
    if len(tasks) == 0:
        data = {"detail": "Não existe item cadastrado."}
        return JSONResponse(content=data, status_code=status.HTTP_404_NOT_FOUND)
    return tasks


# Retorna uma task
@task.get('/api/tasks/{id}', response_model=TaskRead)
async def get_one(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f"Não existe task com esse ID: {id}")


@task.post('/api/tasks', response_model=TaskRead)
async def create(task: TaskWrite):
    taskFound = await get_one_task_title(task.title)
    if taskFound:
        raise HTTPException(409, "Task com mesmo título já existe.")
    
    task = await create_task(task.dict())
    if task:
        return task
    raise HTTPException(400, "Há algo de errado!")


@task.put('/api/tasks/{id}', response_model=TaskRead)
async def update(id: str, data: UpdateTask):
    task = await update_task(id, data)
    if task:
        return task
    raise HTTPException(404, f"Não existe task com esse ID: {id}")


@task.delete('/api/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_task(id: str):
    task = await delete_task(id)
    if task:
        return HTTPException(204, "Not Content.")
    raise HTTPException(404, f"Não existe task com esse ID: {id}")