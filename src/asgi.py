import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[dict[str, Any] | None]:
    with SQLModelDatabase(os.environ["DATABASE_URL"]) as db:
        _app.state.db = db
        yield


app = FastAPI(lifespan=lifespan)
