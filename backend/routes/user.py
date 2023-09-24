from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.responses import JSONResponse
from models import UserRead, UserWrite, UserUpdate, UserLogin, UserAccess
from database import get_users_all, get_one_user_id, create_new_user, \
    update_user, delete_user, get_one_user_email
from auth.auth import verify_token, user_validation_login, is_token_blocked, revoke_token

from passlib.context import CryptContext
from decouple import config


user_router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='api/login')

crypt_context = CryptContext(schemes=['sha256_crypt'])

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

# Retorna todos os users
@user_router.get('/api/users')
async def get_users(access_token: str = Depends(verify_token)):
    users = await get_users_all()
    return users


# Retorna um user
@user_router.get('/api/users/{id}', response_model=UserRead)
async def get_one_user(id: str, access_token: str = Depends(verify_token)):
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


# Login
@user_router.post('/api/users/login', response_model=UserAccess)
async def login_user(user: UserLogin):

    is_user_valid = await user_validation_login(user)

    print(is_user_valid)

    if not is_user_valid:
        raise HTTPException(detail=f"Email ou senha inválido.", status_code=status.HTTP_401_UNAUTHORIZED)

    return is_user_valid


# Rota para efetuar logoff (invalidar o token JWT)
@user_router.post('/api/users/logoff')
async def logout(token: str = Depends(OAuth2PasswordBearer(tokenUrl='api/login')), access_token: str = Depends(verify_token)):
    # Neste exemplo, adicionamos o token à lista negra
    # Em um aplicativo real, você deve armazenar e consultar essa lista de maneira mais eficiente
    revoke_token(token)
    if is_token_blocked(token):
        raise HTTPException(status_code=200, detail="Token invalidado com sucesso")






