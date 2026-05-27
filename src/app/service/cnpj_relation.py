from app.dto.cnpj_relation import CnpjRelationDTO
from app.presenter.cnpj_relation import CnpjRelationPresenter
from app.repository.cnpj_relation import CnpjRelationRepository


class CnpjRelationService:
    """
    Centralizador de lógica e regras de negócio do projeto.
    """

    def __init__(self, repository: CnpjRelationRepository) -> None:
        self.repository = repository
        self.presenter = CnpjRelationPresenter()

    def get_found_relations(self, supplier_cnpj: str | None) -> CnpjRelationDTO | None:
        if not (model := self.repository.get(supplier_cnpj=supplier_cnpj)):
            return None

        return self.presenter.present(model=model)

    def register_relations(self, data: CnpjRelationDTO) -> CnpjRelationDTO | None:
        if not (model := self.repository.create(data=data)):
            return None

        return self.presenter.present(model=model)
