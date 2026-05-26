from pydantic import BaseModel


class CnpjRelationRequestDTO(BaseModel):
    """Dados para cadastro de relação de CNPJs."""

    cnpj: str
    """CNPJ do fornecedor filial."""

    parent_cnpj: str
    """CNPJ do fornecedor matriz."""
