from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated

from app.dto.cnpj_relation import CnpjRelationDTO
from app.service.cnpj_relation import CnpjRelationService
from dependencies import get_cnpj_relation_service

router = APIRouter(prefix="/cnpj_relation")


@router.get("/list/{supplier_cnpj}", summary="Listar relações de CNPJs")
def list_relations(
    service: Annotated[CnpjRelationService, Depends(get_cnpj_relation_service)],
    supplier_cnpj: str | None = None,
) -> CnpjRelationDTO | None:
    if not (response := service.get_found_relations(config_name=supplier_cnpj)):
        raise HTTPException(status_code=404, detail=f"Nenhuma relação encontrada para o CNPJ [{supplier_cnpj}].")

    return response


@router.post("/register", summary="Registrar nova relação entre CNPJs")
def register_relation(
    service: Annotated[CnpjRelationService, Depends(get_cnpj_relation_service)],
    register_dto: CnpjRelationDTO,
) -> CnpjRelationDTO:
    if service.get_found_relations(config_name=register_dto.cnpj):
        raise HTTPException(status_code=409, detail="Relação entre CNPJs já cadastrada.")

    if not (response := service.register_relations(data=register_dto)):
        raise HTTPException(status_code=400, detail="Erro ao registrar integração.")

    return response
