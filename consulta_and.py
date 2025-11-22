from configuracion import SessionLocal
from crear_base_entidades import Institucion, Publicacion
from sqlalchemy import and_

def consultas_and():
    session = SessionLocal()

    print("=== Instituciones en Guayaquil Y Ecuador ===")
    for inst in session.query(Institucion).filter(
        and_(
            Institucion.ciudad == "Guayaquil",
            Institucion.pais == "Ecuador",
        )
    ).all():
        print(inst.nombre, "-", inst.ciudad, "-", inst.pais)

    print("\n=== Artículos del año 2024 ===")
    for pub in session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.fecha_publicacion.like("2024-%"),
        )
    ).all():
        print(pub.fecha_publicacion, "-", pub.titulo)

    session.close()

if __name__ == "__main__":
    consultas_and()