from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date

from app.database import Base


class Record(Base):
    """
    This is the SQLAlchemy model for the Record table.
    """
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String(20), index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)
