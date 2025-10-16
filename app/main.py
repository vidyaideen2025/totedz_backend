from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI(title="Totedz Education Portal")

# Register routers
app.include_router(health.router)