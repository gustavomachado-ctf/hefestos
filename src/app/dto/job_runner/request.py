from pydantic import BaseModel


class JobRunnerRequestDTO(BaseModel):
    name: str
    task_definition_id: str
    capacity_provider: str = "FARGATE"
    container_name: str
    subnets: str
    security_group: str
