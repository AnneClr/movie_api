from typing import List
from fastapi import Depends, FastAPI, HTTPException
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


@app.get("/movies/{movie_year}", response_model=List[schema.Movie])
def get_by_year(movie_year: int, db: Session = Depends(get_db)):
    movie_by_year = crud.get_by_year(db, movie_year=movie_year)
    if movie_by_year is None:
        raise HTTPException(status_code=404, detail="The {movie_by_year} not found")
    return movie_by_year


@app.get("/movie/{movie_id}", response_model=schema.Movie)
def get_by_id(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_by_id(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie
