from fastapi import APIRouter,  Body, Request, Response, HTTPException, status, FastAPI
from fastapi.encoders import jsonable_encoder

from app.src.db import db


app = FastAPI(
         title="Fake API",
         description="MXM - MAXIMO",
         version="0.0.1"
     )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/centro_custo', response_description="Get a centro custo")
async def find_centro_custo():
    return db.fake_centro_custo
