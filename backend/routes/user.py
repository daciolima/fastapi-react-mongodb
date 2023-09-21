from fastapi import HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from models import UserRead, UserWrite, UserUpdate, LoginUser
from database import get_users_all, get_one_user_id, create_new_user, \
    update_user, delete_user, get_one_user_email
from passlib.context import CryptContext
# from passlib.hash import sha256_crypt

user_router = APIRouter()

crypt_context = CryptContext(schemes=['sha256_crypt'])


# Retorna todos os users
@user_router .get('/api/users')
async def get_users():
    users = await get_users_all()
    return users


# Retorna um user
@user_router.get('/api/users/{id}', response_model=UserRead)
async def get_one_user(id: str):
    user = await get_one_user_id(id)
    if user:
        return user
    raise HTTPException(404, f"Não existe user com esse ID: {id}")


@user_router.post('/api/users', response_model=UserRead)
async def create_user(user: UserWrite):
    user.password = crypt_context.hash(user.password)
    # user_password = sha256_crypt.hash(user.password)
    
    userExist= await get_one_user_email(user.email)
    if userExist:
        raise HTTPException(409, "user com mesmo email já existe.")
    
    # new_user = {
    #     'nome': user.nome,
    #     'email': user.email,
    #     'password': user_password,
    # }

    # user = await create_new_user(new_user)
    user = await create_new_user(user.dict())

    if user:
        print(user)
        return JSONResponse(content={'detail': f"User {user['email']} criado com sucesso!"}, status_code=status.HTTP_201_CREATED)
    raise HTTPException(400, "Há algo de errado!")


@user_router.put('/api/users/{id}', response_model=UserRead)
async def update(id: str, data: UserUpdate):
    user = await update_user(id, data)
    if user:
        return user
    raise HTTPException(404, f"Não existe user com esse ID: {id}")


@user_router.delete('/api/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(id: str):
    user = await delete_user(id)
    if user:
        return HTTPException(204, "Not Content.")
    raise HTTPException(404, f"Não existe user com esse ID: {id}")

# # Login
# @user_router.post('/api/users/login', response_model=UserRead)
# async def login_user(user: LoginUser):
#     user = await access_login_user(id)
#     if user:
#         return user
#     raise HTTPException(404, f"Não existe user com esse ID: {id}")