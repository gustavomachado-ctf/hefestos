from sqlmodel import Session, select

from app.dto.register import RegisterDTO
from app.model.register import RegisterModel


class RegisterRepository:
    """
    Serviço de banco de dados que utiliza o SQLModel e SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, config_name: str | None) -> list[RegisterModel] | None:
        try:
            statement = select(RegisterModel)

            if config_name:
                statement = select(RegisterModel).where(RegisterModel.name == config_name)

            return self.session.exec(statement).all() or None

        except Exception:
            self.session.rollback()
            raise

    def create(self, data: RegisterDTO) -> list[RegisterModel] | None:
        try:
            model = RegisterModel(**data.model_dump())

            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)

            return None if not model else [model]

        except Exception:
            self.session.rollback()
            raise
