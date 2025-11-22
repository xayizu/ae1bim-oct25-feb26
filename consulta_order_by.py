from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion
from sqlalchemy import asc, desc

def consultas_order_by():
    session = SessionLocal()

    print("=== Investigadores ordenados por apellido (A-Z) ===")
    for inv in session.query(Investigador).order_by(asc(Investigador.apellido)).all():
        print(inv.apellido, inv.nombre)

    print("\n=== Publicaciones por fecha (viejas primero) ===")
    for pub in session.query(Publicacion).order_by(Publicacion.fecha_publicacion).all():
        print(pub.fecha_publicacion, "-", pub.titulo)

    print("\n=== Publicaciones por fecha (nuevas primero) ===")
    for pub in session.query(Publicacion).order_by(desc(Publicacion.fecha_publicacion)).all():
        print(pub.fecha_publicacion, "-", pub.titulo)

    session.close()

if __name__ == "__main__":
    consultas_order_by()