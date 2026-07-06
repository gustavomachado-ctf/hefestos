from sqlmodel import SQLModel, Field


class CnpjRelationModel(SQLModel, table=True):
    """Modelo para cadastro da relação entre CNPJs."""

    cnpj: str = Field(min_length=14, max_length=14, primary_key=True, nullable=False)
    """CNPJ do fornecedor filial."""

    parent_cnpj: str = Field(min_length=14, max_length=14, nullable=False)
    """CNPJ do fornecedor matriz."""
