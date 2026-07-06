from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Query

from app.dto.job_runner import JobRunnerDTO
from app.service.job_runner import JobRunnerService
from dependencies import get_job_runner_service

router = APIRouter(prefix="/job_runner")


@router.get("/list", summary="Listar Runners")
def list_runners(
    service: Annotated[JobRunnerService, Depends(get_job_runner_service)],
    config_name: str | None = Query(default=None),
) -> list[JobRunnerDTO] | None:
    if not (response := service.get_found_runners(config_name=config_name)):
        raise HTTPException(status_code=404, detail="Job Runner não encontrado.")

    return response


@router.post("/register", summary="Registrar Job Runner")
def register_runner(
    service: Annotated[JobRunnerService, Depends(get_job_runner_service)],
    job_runner_dto: JobRunnerDTO,
) -> JobRunnerDTO:
    if service.get_found_runners(config_name=job_runner_dto.name):
        raise HTTPException(status_code=409, detail="Job Runner já cadastrada.")

    if not (response := service.register_runner(data=job_runner_dto)):
        raise HTTPException(status_code=400, detail="Erro ao registrar Job Runner.")

    return response
