from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a la base de datos SQLite (puedes cambiarla por otra base de datos si prefieres)
DATABASE_URL = "sqlite:///./test.db"  # Cambia esto si quieres usar otro motor de base de datos

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Crear una base de datos declarativa


# Crear un sessionmaker que nos permita interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()