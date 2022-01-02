from fastapi import FastAPI
from src.infra.routes import health


def init_app(app: FastAPI):
    app.include_router(health.router)