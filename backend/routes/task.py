from fastapi import HTTPException, status, APIRouter
from database import get_all_tasks, get_one_task_id, create_task, update_task, delete_task, get_one_task_title
from models import TaskRead, TaskWrite, TaskUpdate

task_router = APIRouter()


# Retorno Raiz
@task_router.get('/')
def welcome():
    return {'message': 'Bem-vindo ao FastAPI'}


# Retorna todas as tasks
@task_router.get('/api/tasks')
async def get_all():
    tasks = await get_all_tasks()
    return tasks


# Retorna uma task
@task_router.get('/api/tasks/{id}', response_model=TaskRead)
async def get_one(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f"Não existe task com esse ID: {id}")


@task_router.post('/api/tasks', response_model=TaskRead)
async def create(task: TaskWrite):
    taskFound = await get_one_task_title(task.title)
    if taskFound:
        raise HTTPException(409, "Task com mesmo título já existe.")
    
    task = await create_task(task.dict())
    if task:
        return task
    raise HTTPException(400, "Há algo de errado!")


@task_router.put('/api/tasks/{id}', response_model=TaskRead)
async def update(id: str, data: TaskUpdate):
    task = await update_task(id, data)
    if task:
        return task
    raise HTTPException(404, f"Não existe task com esse ID: {id}")


@task_router.delete('/api/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_task(id: str):
    task = await delete_task(id)
    if task:
        return HTTPException(204, "Not Content.")
    raise HTTPException(404, f"Não existe task com esse ID: {id}")