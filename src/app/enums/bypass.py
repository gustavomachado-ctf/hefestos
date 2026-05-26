from enum import StrEnum


class BypassFieldsEnum(StrEnum):
    """Enum com os campos de onde o desvio pode ser passado para a integração."""

    access_url = "URL_ACESSO"
    aux_code = "CODIGO_AUXILIAR"
