from sqlmodel import SQLModel, Field


class CnpjRelationsModel(SQLModel, table=True):
    """Modelo para cadastro da relação entre CNPJs."""

    cnpj: str = Field(min_length=14, max_length=14, nullable=False)
    """CNPJ do fornecedor filial."""

    parent_cnpj: str = Field(min_length=14, max_length=14, nullable=False)
    """CNPJ do fornecedor matriz."""
