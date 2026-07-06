import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from app.controller.job_runner import router as job_runner
from app.controller.register import router as register_router
from app.repository.database import SQLModelDatabase


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[dict[str, Any] | None]:
    with SQLModelDatabase(os.environ["DATABASE_URL"]) as db:
        _app.state.db = db
        yield


app = FastAPI(lifespan=lifespan)

app.include_router(register_router)
app.include_router(job_runner)
