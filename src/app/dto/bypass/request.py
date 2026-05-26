from enum import StrEnum

from pydantic import BaseModel


class BypassFields(StrEnum):
    """Enum com os campos de onde o desvio pode ser passado para a integração."""

    access_url = "URL_ACESSO"
    aux_code = "CODIGO_AUXILIAR"


class BypassRequestDTO(BaseModel):
    """Dados para cadastro de desvio."""

    name: str
    """Nome do desvio (nome integração + campo utilizado no desvio)."""

    base_config_name: str | None = None
    """Nome da integração base a ser utilizada como referência."""

    name_config_hecate: str
    """Nome da configuração no Hecate."""

    bypass_field: BypassFields
    """Campo de onde o desvio pode ser passado para a integração."""

    comparator: str = "ILIKE"
    """Comparador a ser utilizado no campo para verificar o valor."""

    value: str
    """Valor a ser verificado no campo (flag do desvio)."""
