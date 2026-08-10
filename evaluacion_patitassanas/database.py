"""
database.py
Centro Veterinario PatitasSanas
------------------------------------------------
Este módulo se encarga de crear la base de datos SQLite
'patitassanas.db' y la tabla 'pacientes', según el diseño
de datos ya aprobado por el analista del proyecto.
"""

import sqlite3

DB_NAME = "patitassanas.db"


def crear_conexion():
    """Crea y retorna una conexión a la base de datos SQLite."""
    conexion = sqlite3.connect(DB_NAME)
    # Permite acceder a las columnas de los resultados por nombre (fila tipo diccionario)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_base_datos():
    """
    Crea la base de datos y la tabla 'pacientes' si no existen.

    Atributos según el diseño aprobado:
    - id: entero, clave primaria autoincremental
    - nombre_mascota: texto, obligatorio
    - especie: texto, obligatorio
    - edad: entero, debe ser mayor o igual a 0
    - nombre_propietario: texto, obligatorio
    - telefono_propietario: texto, obligatorio
    """
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # Se usa "CREATE TABLE IF NOT EXISTS" para que, al ejecutar la app varias
    # veces, la tabla no se duplique ni genere errores.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_mascota TEXT NOT NULL,
            especie TEXT NOT NULL,
            edad INTEGER NOT NULL CHECK (edad >= 0),
            nombre_propietario TEXT NOT NULL,
            telefono_propietario TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()
    print(f"Base de datos '{DB_NAME}' y tabla 'pacientes' verificadas/creadas correctamente.")


if __name__ == "__main__":
    # Permite ejecutar este archivo de forma independiente para crear la BD
    crear_base_datos()
