# Django CRUD Formulario

Este proyecto demuestra cómo crear un sistema CRUD (Crear, Leer, Actualizar, Eliminar) utilizando formularios en Django. Se enfoca en la gestión de contactos, donde puedes añadir, visualizar, editar y eliminar contactos de una base de datos.

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instalación

1. **Clona este repositorio:**

    ```bash
    git clone https://github.com/danielschez/contactos.git
    cd catalogo_contacto
    ```

2. **Crea y activa un entorno virtual:**

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # En macOS/Linux
    # myenv\Scripts\activate  # En Windows
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Realiza las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

5. **Inicia el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

6. **Accede a la aplicación en tu navegador:**

    ```plaintext
    http://127.0.0.1:8000/
    ```

## Modelos

El proyecto incluye un modelo principal:

- `Contacto`: Representa a un contacto con campos como `nombre`, `apellidoPaterno`, `apellidoMaterno`, `fechaNacimiento`, `alias`, `email`, `telefono`, `direccion`, entre otros.

## Vistas

El proyecto implementa las siguientes vistas CRUD:

- **Crear**: Permite añadir un nuevo contacto.
- **Leer**: Muestra una lista de todos los contactos.
- **Actualizar**: Permite editar la información de un contacto existente.
- **Eliminar**: Permite borrar un contacto.

## Formularios