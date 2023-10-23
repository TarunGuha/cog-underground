from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.router import router as main_router

docs = {"title": "COG Underground", "docs_url": "/docs"}
app = FastAPI(**docs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)

handler = Mangum(app)
