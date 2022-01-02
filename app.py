from fastapi import FastAPI

from src.config import routes


def create_app() -> FastAPI:
    app = FastAPI()
    routes.init_app(app)
    return app


app = create_app()