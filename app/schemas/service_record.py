from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ServiceRecordCreate(BaseModel):
    title: str
    description: Optional[str] = None
    service_date: date
    odometer: int = Field(ge=0)
    cost: Optional[float] = Field(default=None, ge=0)
    provider: Optional[str] = None


class ServiceRecordUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    service_date: date
    odometer: int = Field(ge=0)
    cost: Optional[float] = Field(default=None, ge=0)
    provider: Optional[str] = None


class ServiceRecordResponse(BaseModel):
    id: int
    vehicle_id: int
    title: str
    description: Optional[str]
    service_date: date
    odometer: int
    cost: Optional[float]
    provider: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)