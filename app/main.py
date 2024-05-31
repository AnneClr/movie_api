from typing import List
from fastapi import Depends, FastAPI
from app import crud
import app.schema as schema
from .database import SessionLocal, engine
from app import database
from sqlalchemy.orm import Session

# Mise en place de l'ORM, création d'un engine
database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
# On crée une connexion avec la base de données qu'on stocke dans db
# Le close est géré directement dans cette fonction
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies", response_model=List[schema.Movie])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db)
