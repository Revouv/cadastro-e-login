import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-de-desenvolvimento")
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 30


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def create_token(email):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    return jwt.encode({"sub": email, "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])["sub"]
