from enum import StrEnum


class BypassFieldsEnum(StrEnum):
    """Enum com os campos de onde o desvio pode ser passado para a integração."""

    URL_ACESSO = "URL_ACESSO"
    CODIGO_AUXILIAR = "CODIGO_AUXILIAR"
