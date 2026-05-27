from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.repository.bypass import ByPassRepository
from app.repository.cnpj_relation import CnpjRelationRepository
from app.repository.database import SQLModelDatabase
from app.repository.job_runner import JobRunnerRepository
from app.repository.register import RegisterRepository
from app.service.bypass import ByPassService
from app.service.cnpj_relation import CnpjRelationService
from app.service.job_runner import JobRunnerService
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


def get_job_runner_session_service() -> Generator[JobRunnerRepository]:
    with SQLModelDatabase.get_session() as session:
        yield JobRunnerRepository(session)


def get_cnpj_relation_session_service() -> Generator[CnpjRelationRepository]:
    with SQLModelDatabase.get_session() as session:
        yield CnpjRelationRepository(session)


def get_register_service(repository: RegisterDatabaseDependecy) -> RegisterService:
    return RegisterService(repository)


def get_bypass_service(repository: ByPassDatabaseDependecy) -> ByPassService:
    return ByPassService(repository)


def get_job_runner_service(repository: JobRunnerDatabaseDependecy) -> JobRunnerService:
    return JobRunnerService(repository)


def get_cnpj_relation_service(repository: CnpjRelationDatabaseDependecy) -> CnpjRelationService:
    return CnpjRelationService(repository)


DatabaseDependency = Annotated[Session, Depends(get_database_session_service)]
RegisterDatabaseDependecy = Annotated[RegisterRepository, Depends(get_register_session_service)]
ByPassDatabaseDependecy = Annotated[ByPassRepository, Depends(get_bypass_session_service)]
JobRunnerDatabaseDependecy = Annotated[JobRunnerRepository, Depends(get_job_runner_session_service)]
CnpjRelationDatabaseDependecy = Annotated[CnpjRelationRepository, Depends(get_cnpj_relation_session_service)]
