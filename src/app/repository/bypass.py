from sqlmodel import Session, select

from app.dto.bypass import ByPassDTO
from app.model.bypass import ByPassModel


class ByPassRepository:
    """
    Serviço de banco de dados que utiliza o SQLModel e SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, config_name: str | None) -> ByPassModel | None:
        try:
            statement = select(ByPassModel)

            if config_name:
                statement = select(ByPassModel).where(ByPassModel.base_config_name == config_name)

            return self.session.exec(statement).first()

        except Exception:
            self.session.rollback()
            raise

    def create(self, data: ByPassDTO) -> ByPassModel | None:
        try:
            model = ByPassModel(**data.model_dump())

            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)

            return model

        except Exception:
            self.session.rollback()
            raise
