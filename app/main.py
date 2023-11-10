from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.database import Base, SessionLocal, engine
from app.models import Record
from app.schemas import RecordSchema


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*']
)


# Dependency
def get_db():
    """
    This function returns a new SQLAlchemy SessionLocal object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home():
    """
    This function redirects the user to the API documentation page.
    """
    return RedirectResponse(url='/docs/')


@app.get('/records', response_model=List[RecordSchema])
def get_all_records(db: Session = Depends(get_db)):
    """
    This function returns all records in the database.
    """
    records = db.query(Record).all()
    return records
