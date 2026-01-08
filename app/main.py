from fastapi import FastAPI
from app.database import engine, Base
from app.api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GitHub Repo Manager")

app.include_router(router)
