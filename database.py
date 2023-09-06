# motor => Lib permite consultas assincronas
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
import pymongo
from models import Task
from bson import ObjectId


# Config para MongoDB
# user_mongo: settings.user_mongo
# password_mongo: str = "root"
# address_mongo: str = "localhost"
# port_mongo: int = 27017
# URI_MONGO: str = f"mongodb://{user_mongo}:{password_mongo}@{address_mongo}:{port_mongo}/?authMechanism=DEFAULT"


try:
    # Conexão com o banco
    connection_mongo = f"mongodb://{config('USER_MONGO')}:{config('PASSWD_MONGO')}@{config('ADDRESS_MONGO')}:{config('PORT_MONGO')}/?authMechanism=DEFAULT"
    client = AsyncIOMotorClient(connection_mongo)
    print('Conectado ao mongoDB')
    # Criando um keyspace
    database = client.tasks_database

    # Criando uma coleção
    CollectionTask = database.tasks

    # Criando index
    CollectionTask.create_index([("title", pymongo.ASCENDING)], unique=True)


except Exception as err:
    raise err



# Fn de write e read ao MongoDB
# Retornando um elemento
async def get_one_task_id(id):
    task = await CollectionTask.find_one({'_id': ObjectId(id)})
    return task

async def get_one_task_title(title):
    task = await CollectionTask.find_one({'title': title})
    return task

# Retorna todos os elementos
async def get_all_tasks():
    tasks = []
    cursor = CollectionTask.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks
    # return [task async for task in CollectionTask.find({})]

# Criando um elemento
async def create_task(task):
    new_task = await CollectionTask.insert_one(task)
    created_task = await CollectionTask.find_one({'_id': new_task.inserted_id})
    return created_task

# Atualizando um elemento
async def update_task(id: str, task):
    await CollectionTask.update_one({'_id': id}, {'$set': task})
    document = await CollectionTask.find_one({'_id': id})
    return document

# delete um elemento
async def delete_task(id: str):
    await CollectionTask.delete_one({'_id': id})
    return True


