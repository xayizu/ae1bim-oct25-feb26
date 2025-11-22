from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def mostrar_todo():
    session = SessionLocal()

    print("=== INSTITUCIONES ===")
    for inst in session.query(Institucion).all():
        print(inst.id, inst.nombre, inst.ciudad, inst.pais)

    print("\n=== DEPARTAMENTOS ===")
    for dep in session.query(Departamento).all():
        print(dep.id, dep.nombre, dep.codigo, "->", dep.institucion.nombre)

    print("\n=== INVESTIGADORES ===")
    for inv in session.query(Investigador).all():
        print(inv.id, inv.nombre, inv.apellido, "->", inv.departamento.nombre)

    print("\n=== PUBLICACIONES ===")
    for pub in session.query(Publicacion).all():
        print(pub.id, pub.titulo, "->", pub.investigador.nombre, pub.investigador.apellido)

    session.close()

if __name__ == "__main__":
    mostrar_todo()