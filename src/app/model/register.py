from sqlmodel import Field, SQLModel


class RegisterBaseModel(SQLModel):
    """Modelo para cadastro de integração."""

    name: str = Field(min_length=1, max_length=100, primary_key=True)
    """Nome da integração."""

    cnpj: str = Field(min_length=14, max_length=14, nullable=True)
    """CNPJ do fornecedor."""

    bucket_name: str = Field(min_length=1, max_length=50, nullable=True)
    """Bucket da integração."""

    payment_condition_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de pagamento."""

    aux_queue: str | None = Field(max_length=100)
    """Fila auxiliar."""

    general_queue: str | None = Field(max_length=100, nullable=True)
    """Fila geral."""

    order_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de pedido."""

    authentication_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de autenticação."""

    price_ingestion_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de ingestão."""

    pedpreco_order_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de pedido do Pedpreco."""

    pedpreco_invoice_queue: str | None = Field(max_length=100, nullable=True)
    """Fila de retorno do Pedpreco."""

    job_runner_name: str | None = Field(max_length=100, nullable=True)
    """Nome do Job Runner criado para a integração."""

    use_protheus: bool = Field(default=True)
    """Sinalizar se a integração usa Protheus para conversão de DTOs."""

class RegisterModel(RegisterBaseModel, table=True):
    """
    Representa a tabela de registro das integrações.
    """

    __tablename__ = "configs"
