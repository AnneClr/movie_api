# Pas dans une classe, donc il faut faire une injection de session
from sqlalchemy.orm import Session

from app import entity


def save(db: Session):
    pass


# On récupère tous les films
# on passe une classe en paramètre (c'est dans cette classe qu'on renseigne le nom de la table)
# il faut convertir l'entity Movie en schemas Movie => fait automatiquement avec la class Config déclarée dans schema.py
def get_all(db: Session):
    return db.query(entity.Movie).all()


def get_by_id(db: Session, movie_id: int):
    return db.query(entity.Movie).get(movie_id)


def get_by_year(db: Session, movie_year: int):
    return db.query(entity.Movie).filter(entity.Movie.year == movie_year).all()


def get_by_title(db: Session, movie_title: str):
    return db.query(entity.Movie).filter(entity.Movie.title == movie_title).all()
