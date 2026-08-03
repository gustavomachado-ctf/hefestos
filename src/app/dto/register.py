from pydantic import BaseModel


class RegisterDTO(BaseModel):
    """Dados para cadastro de nova integração."""

    name: str
    """Nome da integração."""

    cnpj: str | None = None
    """CNPJ do fornecedor."""

    bucket_name: str | None = None
    """Bucket da integração."""

    payment_condition_queue: str | None = None
    """Fila de pagamento."""

    aux_queue: str | None = None
    """Fila auxiliar."""

    general_queue: str | None = None
    """Fila geral."""

    order_queue: str | None = None
    """Fila de pedido."""

    authentication_queue: str | None = None
    """Fila de autenticação."""

    price_ingestion_queue: str | None = None
    """Fila de ingestão."""

    pedpreco_order_queue: str | None = None
    """Fila de pedido do Pedpreco."""

    pedpreco_invoice_queue: str | None = None
    """Fila de retorno do Pedpreco."""

    job_runner_name: str | None = None
    """Nome do Job Runner criado para a integração."""

    use_protheus: bool = True
    """Sinalizar se a integração usa Protheus para conversão de DTOs."""
