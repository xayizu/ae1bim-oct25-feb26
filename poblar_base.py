# poblar_base.py
from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def poblar_datos():
    session = SessionLocal()

    try:
        # 1) Instituciones
        espol = Institucion(nombre="ESPOL", ciudad="Guayaquil", pais="Ecuador")
        utpl = Institucion(nombre="UTPL", ciudad="Loja", pais="Ecuador")
        session.add_all([espol, utpl])
        session.flush()

        # 2) Departamentos
        d_cs_esp = Departamento(nombre="Ciencias de la Computación", codigo="CC01", institucion=espol)
        d_teleco_esp = Departamento(nombre="Telecomunicaciones", codigo="TEL02", institucion=espol)
        d_sis_utpl = Departamento(nombre="Ingeniería de Sistemas", codigo="IS01", institucion=utpl)
        d_edu_utpl = Departamento(nombre="Educación", codigo="EDU01", institucion=utpl)
        session.add_all([d_cs_esp, d_teleco_esp, d_sis_utpl, d_edu_utpl])
        session.flush()

        # 3) Investigadores
        inv1 = Investigador(
            nombre="Ana",
            apellido="Pérez",
            email="ana.perez@espol.edu.ec",
            area_investigacion="Inteligencia Artificial",
            departamento=d_cs_esp
        )
        inv2 = Investigador(
            nombre="Luis",
            apellido="González",
            email="luis.gonzalez@espol.edu.ec",
            area_investigacion="Redes y Seguridad",
            departamento=d_teleco_esp
        )
        inv3 = Investigador(
            nombre="María",
            apellido="Lozano",
            email="maria.lozano@utpl.edu.ec",
            area_investigacion="Educación Virtual",
            departamento=d_edu_utpl
        )
        inv4 = Investigador(
            nombre="Carlos",
            apellido="Ramírez",
            email="carlos.ramirez@utpl.edu.ec",
            area_investigacion="Desarrollo Web",
            departamento=d_sis_utpl
        )
        session.add_all([inv1, inv2, inv3, inv4])
        session.flush()

        # 4) Publicaciones
        pub1 = Publicacion(
            titulo="Aplicaciones de IA en educación superior",
            fecha_publicacion="2023-05-10",
            doi="10.1000/ia-edu-2023",
            tipo_publicacion="Artículo",
            investigador=inv1
        )
        pub2 = Publicacion(
            titulo="Arquitecturas seguras para redes universitarias",
            fecha_publicacion="2022-11-20",
            doi="10.1000/redes-2022",
            tipo_publicacion="Conferencia",
            investigador=inv2
        )
        pub3 = Publicacion(
            titulo="Modelos híbridos de educación virtual",
            fecha_publicacion="2024-01-15",
            doi="10.1000/edu-virtual-2024",
            tipo_publicacion="Artículo",
            investigador=inv3
        )
        pub4 = Publicacion(
            titulo="Buenas prácticas en desarrollo de aplicaciones web",
            fecha_publicacion="2024-06-01",
            doi=None,
            tipo_publicacion="Tesis",
            investigador=inv4
        )
        session.add_all([pub1, pub2, pub3, pub4])

        session.commit()
        print("✅ Datos de ejemplo insertados correctamente.")

    except Exception as e:
        session.rollback()
        print("❌ Error al poblar la base de datos:", e)
    finally:
        session.close()


if __name__ == "__main__":
    poblar_datos()