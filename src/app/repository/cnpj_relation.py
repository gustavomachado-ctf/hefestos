from sqlmodel import Session, select

from app.dto.cnpj_relation import CnpjRelationDTO
from app.model.cnpj_relations import CnpjRelationModel


class CnpjRelationRepository:
    """
    Serviço de banco de dados que utiliza o SQLModel e SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, supplier_cnpj: str | None) -> list[CnpjRelationModel] | None:
        try:
            statement = select(CnpjRelationModel)

            if supplier_cnpj:
                statement = (
                    select(CnpjRelationModel).where(
                        (CnpjRelationModel.cnpj == supplier_cnpj) |
                        (CnpjRelationModel.parent_cnpj == supplier_cnpj)
                    ))

            return self.session.exec(statement).all() or None

        except Exception:
            self.session.rollback()
            raise

    def create(self, data: CnpjRelationDTO) -> list[CnpjRelationModel] | None:
        try:
            model = CnpjRelationModel(**data.model_dump())

            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)

            return model or None

        except Exception:
            self.session.rollback()
            raise
