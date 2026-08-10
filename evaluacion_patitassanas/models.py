"""
models.py
Centro Veterinario PatitasSanas
------------------------------------------------
Funciones CRUD (Crear, Leer, Actualizar, Eliminar) para
la tabla 'pacientes', siguiendo el diseño ya aprobado.
"""

from database import crear_conexion


def registrar_paciente(nombre_mascota, especie, edad, nombre_propietario, telefono_propietario):
    """
    Registra un nuevo paciente en la base de datos.

    MEDIDA DE SEGURIDAD 1 (Inyección SQL):
    Se utiliza una consulta parametrizada con marcadores de posición (?)
    en lugar de concatenar directamente los valores del formulario dentro
    de la cadena SQL. Esto evita que un usuario malicioso pueda inyectar
    código SQL a través de los campos del formulario.
    """
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO pacientes
            (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario)
    )
    conexion.commit()
    conexion.close()


def listar_pacientes():
    """Retorna la lista completa de pacientes registrados, ordenados por id."""
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre_mascota, especie, edad, nombre_propietario, telefono_propietario FROM pacientes ORDER BY id")
    pacientes = cursor.fetchall()
    conexion.close()
    return pacientes


def eliminar_paciente(id_paciente):
    """
    Elimina un paciente de la base de datos según su id.
    También usa consulta parametrizada por la misma razón de seguridad
    explicada en registrar_paciente().
    """
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_paciente,))
    conexion.commit()
    conexion.close()


def actualizar_paciente(id_paciente, nombre_mascota, especie, edad, nombre_propietario, telefono_propietario):
    """
    (Opcional) Actualiza los datos de un paciente existente.
    Consulta parametrizada por la misma razón de seguridad explicada arriba.
    """
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE pacientes
        SET nombre_mascota = ?, especie = ?, edad = ?, nombre_propietario = ?, telefono_propietario = ?
        WHERE id = ?
        """,
        (nombre_mascota, especie, edad, nombre_propietario, telefono_propietario, id_paciente)
    )
    conexion.commit()
    conexion.close()
