# crear_base_entidades.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import Base, engine


class Institucion(Base):
    __tablename__ = "instituciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    pais = Column(String(100), nullable=False)

    departamentos = relationship("Departamento", back_populates="institucion")


class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(50), nullable=False)

    institucion_id = Column(Integer, ForeignKey("instituciones.id"), nullable=False)
    institucion = relationship("Institucion", back_populates="departamentos")

    investigadores = relationship("Investigador", back_populates="departamento")


class Investigador(Base):
    __tablename__ = "investigadores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    area_investigacion = Column(String(150), nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamentos.id"), nullable=False)
    departamento = relationship("Departamento", back_populates="investigadores")

    publicaciones = relationship("Publicacion", back_populates="investigador")


class Publicacion(Base):
    __tablename__ = "publicaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(String(10), nullable=False)  # 'YYYY-MM-DD'
    doi = Column(String(100), nullable=True)
    tipo_publicacion = Column(String(50), nullable=False)  # Artículo, Tesis, etc.

    investigador_id = Column(Integer, ForeignKey("investigadores.id"), nullable=False)
    investigador = relationship("Investigador", back_populates="publicaciones")


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")