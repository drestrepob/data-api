from datetime import date
from pydantic import BaseModel


class RecordSchema(BaseModel):
    id: int
    date: date
    country: str
    cases: int
    deaths: int
    recoveries: int

    class Config:
        from_attributes=True
