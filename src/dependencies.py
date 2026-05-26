from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.repository.database import SQLModelDatabase
from app.repository.register import RegisterRepository
from app.service.register import RegisterService


def get_database_session_service() -> Generator[Session]:
    with SQLModelDatabase.get_session() as session:
        yield session


def get_register_session_service() -> Generator[RegisterRepository]:
    with SQLModelDatabase.get_session() as session:
        yield RegisterRepository(session)


def get_register_service(repository: RegisterDatabaseDependecy) -> RegisterService:
    return RegisterService(repository)


DatabaseDependency = Annotated[Session, Depends(get_database_session_service)]
RegisterDatabaseDependecy = Annotated[RegisterRepository, Depends(get_register_session_service)]
