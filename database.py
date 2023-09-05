# motor => Lib permite consultas assincronas
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings

from models import Task


 # Conexão com o banco
client = AsyncIOMotorClient(settings.URI_MONGO)

# Criando umk keyspace
database = client.tasks_database

# Criando uma coleção
collection = database.tasks



# Fn de write e read ao MongoDB
# Retornando um elemento
async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task

async def get_one_task_title(title):
    task = await collection.find_one({'title': title})
    return task

# Retorna todos os elementos
async def get_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks
    # return [task async for task in collection.find({})]

# Criando um elemento
async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({'id': new_task.inserted_id})
    return created_task

# Atualizando um elemento
async def update_task(id: str, task):
    await collection.update_one({'_id': id}, {'$set': task})
    document = await collection.find_one({'_id': id})
    return document

# delete um elemento
async def delete_task(id: str):
    await collection.delete_one({'_id': id})
    return True


