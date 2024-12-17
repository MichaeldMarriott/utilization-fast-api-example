from fastapi import FastAPI, Query
from models import Utilization
from typing import Annotated
import uuid


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/utilization/{utilization_id}")
async def get_utilization(utilization_id: uuid.UUID):
    return


@app.get("/list-utilizations/{organization_id}")
async def list_utilizations(organization_id: uuid.UUID):
    return


@app.post("/utilization/")
async def create_utilization(
    utilization: Utilization,
    tags: Annotated[
        list[str] | None,
        Query(
            description="Utilization tags",
            title="Tags",)] = None,
):
    return
