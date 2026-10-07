import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

import repository
from schemas import LoginRequest, ProfileResponse, RegisterRequest
from security import DUMMY_HASH, create_token, decode_token, hash_password, verify_password

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest):
    email = data.email.lower()
    if repository.get_user_by_email(email):
        raise HTTPException(status.HTTP_409_CONFLICT, "E-mail já cadastrado")
    repository.create_user(data.name, email, hash_password(data.password))
    return {"message": "Usuário cadastrado com sucesso"}


@router.post("/login")
def login(data: LoginRequest):
    user = repository.get_user_by_email(data.email.strip().lower())
    password_hash = user["password_hash"] if user else DUMMY_HASH
    if not verify_password(data.password, password_hash) or not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "E-mail ou senha inválidos")
    return {"access_token": create_token(user["email"]), "token_type": "bearer"}


def get_current_user(token: str | None = Depends(oauth2_scheme)):
    unauthorized = HTTPException(status.HTTP_401_UNAUTHORIZED, "Token ausente, expirado ou inválido")
    if token is None:
        raise unauthorized
    try:
        email = decode_token(token)
    except jwt.InvalidTokenError:
        raise unauthorized
    user = repository.get_user_by_email(email)
    if not user:
        raise unauthorized
    return user


@router.get("/profile", response_model=ProfileResponse)
def profile(user=Depends(get_current_user)):
    return {"name": user["name"], "email": user["email"]}
