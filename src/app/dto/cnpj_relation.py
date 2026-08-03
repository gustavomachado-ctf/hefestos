from pydantic import BaseModel


class CnpjRelationDTO(BaseModel):
    """Dados para cadastro da relação entre CNPJs."""

    cnpj: str
    """CNPJ do fornecedor filial."""

    parent_cnpj: str
    """CNPJ do fornecedor matriz."""
