from sqlmodel import SQLModel, Field

from app.enums.bypass import BypassFieldsEnum


class ByPassBaseModel(SQLModel):
    """Modelo para cadastrar desvio."""

    name: str = Field(min_length=1, max_length=50, primary_key=True, nullable=False)
    """Nome do desvio."""

    base_config_name: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome da configuração base."""

    config_name: str = Field(min_length=1, max_length=50, nullable=False)
    """Nome da configuração no Hecate."""

    field: BypassFieldsEnum
    """Campo de onde o desvio pode ser passado para a integração."""

    comparator: str = Field(min_length=1, max_length=50, nullable=False)
    """Comparador a ser utilizado no campo para verificar o valor."""

    value: str = Field(min_length=1, max_length=50, nullable=False)
    """flag do desvio que será verificada."""

    regexp_find: str = Field(nullable=True)
    """Eventual regex de validação."""


class ByPassModel(ByPassBaseModel, table=True):
    """
     Representa a tabela de relação entre CNPJ dos fornecedores.
     """

    __tablename__ = "bypasses"
