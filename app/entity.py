from sqlalchemy import Column, Integer, String


# C'est comme du typage mais pas avec des hints mais des fonctions provenont de SQLAlchemy
# On donne des indications sur ce qu'il y a dans la DB
class Movie:
    __tablename__ = "movie"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=300), nullable=False)
    year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=True)
