from configuracion import SessionLocal
from crear_base_entidades import Institucion, Investigador, Publicacion

def consultas_filter():
    session = SessionLocal()

    print("=== Instituciones en Ecuador ===")
    for inst in session.query(Institucion).filter(Institucion.pais == "Ecuador").all():
        print(inst.nombre, "-", inst.ciudad)

    print("\n=== Investigadores de Inteligencia Artificial ===")
    for inv in session.query(Investigador).filter(
        Investigador.area_investigacion == "Inteligencia Artificial"
    ).all():
        print(inv.nombre, inv.apellido)

    print("\n=== Publicaciones de tipo Artículo ===")
    for pub in session.query(Publicacion).filter(
        Publicacion.tipo_publicacion == "Artículo"
    ).all():
        print(pub.titulo)

    session.close()

if __name__ == "__main__":
    consultas_filter()