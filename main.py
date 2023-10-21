from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_ENV

docs = {"title": "COG Underground", "docs_url": "/docs"}
app = FastAPI(**docs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": APP_ENV}


handler = Mangum(app)
