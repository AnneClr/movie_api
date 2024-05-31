from typing import List
from pydantic import BaseModel

# la partie schéma est complètement descriptive, pas besoin de préciser en détail la structure
# le model sert à valider des données échangées en JSON


# Pydantic model
class MovieCreate(
    BaseModel
):  # classe Model hérite de BaseModel (désérialisation des infos de la BDD)
    title: str
    year: int
    duration: int | None


# On crée une classe par forme de JSON échangée càd pour la sérialisation et désérialisation
class Movie(MovieCreate):
    id: int
    # Config est une classe interne, facilite le mapping
    class Config:
        orm_mode = True
