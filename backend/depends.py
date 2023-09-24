from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from decouple import config
from database import get_one_user_email




async def verify_token(access_token: str = Depends(OAuth2PasswordBearer(tokenUrl='api/login'))):

    if is_token_blacklisted(access_token):
        return False
    try:
        data = jwt.decode(access_token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')])
    except JWTError as e:
        return False
    
    user_verify_email = await get_one_user_email(data['sub'])

    if user_verify_email is None:
        return False
    
    return True



oauth_scheme = OAuth2PasswordBearer(tokenUrl='api/login')

def token_verifier(token = Depends(oauth_scheme)):
    
    if not verify_token(token):
        return False
    return True


# Função para verificar se um token está na lista negra (invalidado)
def is_token_blacklisted(token: str):
    # Neste exemplo, usamos uma lista simples de tokens inválidos
    # Em um aplicativo real, você deve armazenar e consultar essa lista de maneira mais eficiente
    fake_access_token = []
    return token in fake_access_token