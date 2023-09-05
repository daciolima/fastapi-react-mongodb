from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from database import get_all_tasks, get_one_task_id, create_task, update_task, delete_task, get_one_task_title
from errors import failed_connection_database
from .models import Task

app = FastAPI()


@app.get('/')
def welcome():
    return {'message': 'Bem-vindo ao FastAPI'}


@app.get('/api/tasks')
async def get_all():
    try:
        tasks = await get_all_tasks()
        if not len(tasks) > 0:
            return JSONResponse(detail="Não existe item.", status_code=status.HTTP_404_NOT_FOUND)
    except:
        return HTTPException(detail=failed_connection_database, status_code=status.HTTP_403_FORBIDDEN)


@app.get('/api/tasks/{id}')
async def get_one():
    try:
        task = await get_one_task_id(id)
        if not len(task) > 0:
            return JSONResponse(detail="Não existe item.", status_code=status.HTTP_404_NOT_FOUND)
    except:
        return HTTPException(detail=failed_connection_database, status_code=status.HTTP_403_FORBIDDEN)


@app.post('/api/tasks', response_model=Task)
async def create(task: Task):
    try:
        taskFound = await get_one_task_title(task.title)
        if taskFound:
            raise HTTPException(409, "Task já existe.")
        
        task = await create_task(task.dict())

        if task:
            return JSONResponse(detail=f"Item {task} cadastrado com sucesso", status_code=status.HTTP_404_NOT_FOUND)
    except:
        return HTTPException(detail=failed_connection_database, status_code=status.HTTP_403_FORBIDDEN)


@app.put('/api/tasks/{id}')
async def update():
    try:
        return {'msg': 'Deleta task'}
    except:
        pass


@app.delete('/api/tasks/{id}')
async def delete():
    try:
        return {'msg': 'Deleta task'}
    except:
        pass