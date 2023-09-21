# motor => Lib permite consultas assincronas
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
import pymongo
from models import TaskRead, TaskUpdate, UserRead
from bson import ObjectId

try:
    # Conexão com o banco
    connection_mongo = f"mongodb://{config('USER_MONGO')}:{config('PASSWD_MONGO')}@{config('ADDRESS_MONGO')}:{config('PORT_MONGO')}/?authMechanism=DEFAULT"
    client = AsyncIOMotorClient(connection_mongo)
    print('Conectado ao mongoDB')
    # Criando keyspaces
    database_tasks = client.tasks_database
    database_users = client.users_database

    # Criando uma coleção
    CollectionTask = database_tasks.tasks
    CollectionUser = database_users.users

    # Criando index
    CollectionTask.create_index([("title", pymongo.ASCENDING)], unique=True)
    CollectionUser.create_index([("email", pymongo.ASCENDING)], unique=True)


except Exception as err:
    raise err


# TRANSATION TASKS
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
        tasks.append(TaskRead(**document))
    return tasks
    # return [task async for task in CollectionTask.find({})]

# Criando um elemento
async def create_task(task):
    new_task = await CollectionTask.insert_one(task)
    created_task = await CollectionTask.find_one({'_id': new_task.inserted_id})
    return created_task

# Atualizando um elemento
async def update_task(id: str, data: TaskUpdate):
    task = {k: v for k, v in data.dict().items() if v is not None}
    await CollectionTask.update_one({'_id': ObjectId(id)}, {'$set': task})
    document = await CollectionTask.find_one({'_id': ObjectId(id)})
    return document

# delete um elemento
async def delete_task(id: str):
    await CollectionTask.delete_one({'_id': ObjectId(id)})
    return True


# TRANSATION USERS

# Fn de write e read ao MongoDB
# Retornando um elemento
async def get_one_user_id(id):
    user = await CollectionUser.find_one({'_id': ObjectId(id)})
    return user

async def get_one_user_email(email):
    user = await CollectionUser.find_one({'email': email})
    return user

# Retorna todos os elementos
async def get_users_all():
    users = []
    cursor = CollectionUser.find({})
    async for document in cursor:
        users.append(UserRead(**document))
    return users
    # return [user async for user in CollectionUser.find({})]

# Criando um elemento
async def create_new_user(user):
    new_user = await CollectionUser.insert_one(user)
    created_user = await CollectionUser.find_one({'_id': new_user.inserted_id})
    return created_user

# Atualizando um elemento
async def update_user(id: str, data: TaskUpdate):
    user = {k: v for k, v in data.dict().items() if v is not None}
    await CollectionUser.update_one({'_id': ObjectId(id)}, {'$set': user})
    document = await CollectionUser.find_one({'_id': ObjectId(id)})
    return document

# delete um elemento
async def delete_user(id: str):
    await CollectionUser.delete_one({'_id': ObjectId(id)})
    return True

# login user
# async def access_login_user(user):
#     user = await CollectionUser.find_one({'email': user.email})
#     if not user:
#         return False
#     if user.password
