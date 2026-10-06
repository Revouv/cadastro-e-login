from fastapi import FastAPI

import repository
from controller import router

repository.create_tables()

app = FastAPI(title="Cadastro e Login")
app.include_router(router)
