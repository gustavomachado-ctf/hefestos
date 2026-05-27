from app.dto.cnpj_relation import CnpjRelationDTO
from app.model.cnpj_relations import CnpjRelationModel


class CnpjRelationPresenter:
    """Apresentação dos dados dos registros."""

    @staticmethod
    def present(model: CnpjRelationModel) -> CnpjRelationDTO:
        return CnpjRelationDTO(**model.model_dump())
