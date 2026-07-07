from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query

from app.dto.job_runner import JobRunnerDTO
from app.dto.register import RegisterDTO
from app.service.job_runner import JobRunnerService
from app.service.register import RegisterService
from dependencies import get_register_service, get_job_runner_service

router = APIRouter(prefix="/integration")


@router.get("/list", summary="Listar Integrações")
def list_integrations(
    service: Annotated[RegisterService, Depends(get_register_service)],
    config_name: str | None = Query(default=None),
) -> list[RegisterDTO] | None:
    if not (response := service.get_found_integrations(config_name=config_name)):
        raise HTTPException(status_code=404, detail="Integração não encontrada.")

    return response


@router.post("/register", summary="Registrar Integração")
def register_integration(
    service: Annotated[RegisterService, Depends(get_register_service)],
    runner_service: Annotated[JobRunnerService, Depends(get_job_runner_service)],
    register_dto: RegisterDTO,
) -> list[RegisterDTO] | list[JobRunnerDTO]:
    if service.get_found_integrations(config_name=register_dto.name):
        raise HTTPException(status_code=409, detail="Integração já cadastrada.")

    if register_dto.job_runner_name:
        if not runner_service.get_found_runners(config_name=register_dto.job_runner_name):
            raise HTTPException(status_code=200, detail="Configuração do Runner não existente, necessária configuração prévia.")

    if not (response := service.register_integration(data=register_dto)):
        raise HTTPException(status_code=400, detail="Erro ao registrar integração.")

    return response
