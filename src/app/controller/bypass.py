from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from app.dto.bypass import ByPassDTO
from app.service.bypass import ByPassService
from dependencies import get_bypass_service

router = APIRouter(prefix="/bypass")


@router.get("/list/{config_name}", summary="Listar desvios.")
def list_bypasses(
    service: Annotated[ByPassService, Depends(get_bypass_service)],
    config_name: str | None = None,
) -> ByPassDTO | None:
    if not (response := service.get_found_deviations(config_name=config_name)):
        raise HTTPException(status_code=404, detail=f"Desvio não encontrado para a integração {config_name}.")

    return response


@router.post("/register", summary="Registrar desvio.")
def register_deviation(
    service: Annotated[ByPassService, Depends(get_bypass_service)],
    bypass_dto: ByPassDTO,
) -> ByPassDTO:
    if service.get_found_deviations(config_name=bypass_dto.name):
        raise HTTPException(status_code=409, detail="desvio já cadastrado.")

    if not (response := service.register_deviation(data=bypass_dto)):
        raise HTTPException(status_code=400, detail="Erro ao registrar desvio.")

    return response
