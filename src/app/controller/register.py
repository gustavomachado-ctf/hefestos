from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated

from app.dto.register import RegisterDTO
from app.service.register import RegisterService
from dependencies import get_register_service

router = APIRouter(prefix="/integration")


@router.get("/list/{config_name}", summary="Listar Integrações")
def list_integrations(
    service: Annotated[RegisterService, Depends(get_register_service)],
    config_name: str | None = None,
) -> RegisterDTO | None:
    if not (response := service.get(config_name=config_name)):
        raise HTTPException(status_code=404, detail="Integração não encontrada")

    return response
