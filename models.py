from pydantic import BaseModel
from datetime import datetime
from enum import Enum
import uuid


class UtilizationType(str, Enum):
    compute = "compute"
    storage = "storage"
    area = "area"
    service = "service"


class Utilization(BaseModel):
    id: uuid.UUID
    service_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    utilization_type: UtilizationType
    duration_ms: float
    value: float
    location_id: uuid.UUID
    internal_user: str
    organization_id: uuid.UUID