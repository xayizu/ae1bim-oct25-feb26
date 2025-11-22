# configuracion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ruta de la base de datos SQLite (archivo local)
DATABASE_URL = "sqlite:///investigacion.db"

# Engine: conexión a la base de datos
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Sesión para interactuar con la BD
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Clase base para los modelos ORM
Base = declarative_base()