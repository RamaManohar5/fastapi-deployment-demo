from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.db import crud
from src.models import models
from src.schemas import schemas
from src.db.database import SessionLocal, engine

# Create the tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db=db)
