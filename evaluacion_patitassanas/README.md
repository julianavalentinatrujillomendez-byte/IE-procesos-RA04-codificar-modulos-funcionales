# Centro Veterinario PatitasSanas — Módulo Gestión de Pacientes

Proyecto desarrollado para el **Instrumento de Evaluación de Conocimientos de Proceso de Codificación**
(SENA — Tecnólogo en Análisis y Desarrollo de Software, código 228118, ficha 3151895).

Codifica el módulo de **Gestión de Pacientes** siguiendo el diseño (modelo de datos y mockup)
ya aprobado por el analista del proyecto.

## Tecnologías
- Python 3.x
- Flask
- SQLite 3
- HTML5 / CSS3

## Estructura del proyecto
```
evaluacion_patitassanas/
├── app.py                 # Rutas Flask
├── database.py             # Creación de la base de datos y tabla pacientes
├── models.py                # Funciones CRUD
├── requirements.txt
├── templates/
│   └── index.html           # Formulario + tabla de pacientes
└── static/
    └── css/
        └── estilos.css       # Estilos propios
```

## Cómo ejecutarlo

1. Crear y activar un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

4. Abrir en el navegador: `http://127.0.0.1:5000/`

Al iniciar, `app.py` crea automáticamente `patitassanas.db` con la tabla `pacientes` si no existe.

## Seguridad aplicada (R4)
1. **Consultas parametrizadas** en todas las operaciones SQL (`models.py`), evitando inyección SQL.
2. **Validación de datos** antes de insertar: campos obligatorios no vacíos y `edad >= 0` (`app.py`).

## Cumplimiento del diseño (mockup)
- Orden de campos del formulario: nombre de la mascota, especie, edad, nombre del propietario, teléfono del propietario.
- Atributos `name` de los inputs iguales a las columnas de la tabla `pacientes`.
- Texto exacto de botones: "Registrar paciente" y "Eliminar".
- Orden de columnas en la tabla: ID, Nombre mascota, Especie, Edad, Propietario, Teléfono, Acción.
