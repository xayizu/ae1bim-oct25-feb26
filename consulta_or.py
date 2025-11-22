from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion
from sqlalchemy import or_

def consultas_or():
    session = SessionLocal()

    print("=== Investigadores de IA O Desarrollo Web ===")
    for inv in session.query(Investigador).filter(
        or_(
            Investigador.area_investigacion == "Inteligencia Artificial",
            Investigador.area_investigacion == "Desarrollo Web",
        )
    ).all():
        print(inv.nombre, inv.apellido, "-", inv.area_investigacion)

    print("\n=== Publicaciones que sean Artículo O Conferencia ===")
    for pub in session.query(Publicacion).filter(
        or_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.tipo_publicacion == "Conferencia",
        )
    ).all():
        print(pub.titulo, "-", pub.tipo_publicacion)

    session.close()

if __name__ == "__main__":
    consultas_or()