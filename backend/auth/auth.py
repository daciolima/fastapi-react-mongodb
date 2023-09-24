from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from decouple import config
from database import get_one_user_email


# from depends import oauth_scheme
from passlib.context import CryptContext
# from passlib.hash import sha256_crypt

crypt_context = CryptContext(schemes=['sha256_crypt'])


async def user_validation_login(user):
    user_verify_email = await get_one_user_email(user.email)

    if user_verify_email is None:
        return False
    
    if not crypt_context.verify(user.password, user_verify_email['password']):
        return False

    print(user_verify_email)


    exp = datetime.utcnow() + timedelta(minutes=int(config('JWT_EXPIRE')))

    payload = {
        'sub': user.email,
        'exp': exp
    }

    # Token a ser enviado para o client
    access_token = jwt.encode(payload, config('SECRET_KEY'), algorithm=config('ALGORITHM'))
    
    return {
        'email': user.email,
        'access_token': access_token,
        'exp': exp.isoformat()
    }

async def verify_token(access_token: str = Depends(OAuth2PasswordBearer(tokenUrl='api/login'))):

    if is_token_blacklisted(access_token):
        raise HTTPException(status_code=401, detail="Token inválido")
    try:
        data = jwt.decode(access_token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')])
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    user_verify_email = await get_one_user_email(data['sub'])

    if user_verify_email is None:
        raise HTTPException(status_code=401, detail="Não foi possível obter o usuário")
    
    return True



oauth_scheme = OAuth2PasswordBearer(tokenUrl='api/login')

def token_verifier(token = Depends(oauth_scheme)):
    
    if not verify_token(token):
        return False
    return True


fake_access_token = []

# Função para verificar se um token está na lista negra (invalidado)
def revoke_token(token: str):
    # Neste exemplo, usamos uma lista simples de tokens inválidos
    # Em um aplicativo real, você deve armazenar e consultar essa lista de maneira mais eficiente
    fake_access_token.append(token)
    print(fake_access_token)
    return token in fake_access_token

# Função para verificar se um token está na lista negra (invalidado)
def is_token_blacklisted(token: str):
    # Neste exemplo, usamos uma lista simples de tokens inválidos
    # Em um aplicativo real, você deve armazenar e consultar essa lista de maneira mais eficiente
    return token in fake_access_token

