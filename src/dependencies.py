from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.repository.bypass import ByPassRepository
from app.repository.database import SQLModelDatabase
from app.repository.register import RegisterRepository
from app.service.bypass import ByPassService
from app.service.register import RegisterService


def get_database_session_service() -> Generator[Session]:
    with SQLModelDatabase.get_session() as session:
        yield session


def get_register_session_service() -> Generator[RegisterRepository]:
    with SQLModelDatabase.get_session() as session:
        yield RegisterRepository(session)


def get_bypass_session_service() -> Generator[ByPassRepository]:
    with SQLModelDatabase.get_session() as session:
        yield ByPassRepository(session)


def get_register_service(repository: RegisterDatabaseDependecy) -> RegisterService:
    return RegisterService(repository)


def get_bypass_service(repository: ByPassDatabaseDependecy) -> ByPassService:
    return ByPassService(repository)


DatabaseDependency = Annotated[Session, Depends(get_database_session_service)]
RegisterDatabaseDependecy = Annotated[RegisterRepository, Depends(get_register_session_service)]
ByPassDatabaseDependecy = Annotated[ByPassRepository, Depends(get_bypass_session_service)]
