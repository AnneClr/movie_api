from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" => utilisé en dev quand on n'a pas de BDD
# SQLALCHEMY_DATABASE_URL = "mariadb+mysqlconnector://movie:password@localhost:3308/dbmovie"
SQLALCHEMY_DATABASE_URL = "postgresql://movie:password@localhost:5432/dbmovie"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
