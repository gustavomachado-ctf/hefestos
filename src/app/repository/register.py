from sqlmodel import Session, select

from app.model.register import RegisterModel


class RegisterRepository:
    """
    Serviço de banco de dados que utiliza o SQLModel e SQLAlchemy.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, config_name: str | None) -> RegisterModel | None:
        statement = select(RegisterModel)

        if config_name:
            statement = select(RegisterModel).where(RegisterModel.name == config_name)

        return self.session.exec(statement).first()
