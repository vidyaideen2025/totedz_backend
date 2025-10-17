from fastapi import FastAPI
from app.api.v1 import health
from app.api.v1.api_router import register_app

app = FastAPI(title="Totedz Education Portal")

# Register routers
register_app(app)
