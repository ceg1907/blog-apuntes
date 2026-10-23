# apuntes.dev

Blog web de apuntes de programación hecho con Django. Es un espacio donde estudiantes comparten lo que van aprendiendo: explicaciones, ejemplos de código y resúmenes de temas de Python, JavaScript, HTML/CSS y Git.

---

## Tecnologías utilizadas

- **Python 3**
- **Django 6.1**: framework web
- **SQLite**: base de datos (viene incluida con Django)
- **Pillow**: manejo de imágenes
- **python-decouple**: lectura de variables de entorno desde el archivo `.env`
- **Markdown**: formato del contenido de los apuntes
- **nh3**: limpieza del HTML generado, para evitar código malicioso en los apuntes
- **HTML y CSS propio**, con Bootstrap Icons y Google Fonts

---

## Funcionalidades principales

**Apuntes (posts)**

- Listado de apuntes en la página de inicio, del más nuevo al más viejo.
- Detalle de cada apunte.
- Crear, editar y eliminar apuntes desde la interfaz web.
- Imagen de portada opcional: si el apunte no tiene imagen, se muestra un recuadro de reemplazo.
- Categorías (Python, JavaScript, HTML/CSS y Git) con filtro desde la barra lateral.
- Contenido con formato **Markdown**: títulos, negritas, listas y bloques de código.
- **Me gusta**: los usuarios registrados pueden dar y quitar like a cada apunte (uno por usuario). La cantidad se ve en el listado y en el detalle.

**Usuarios**

- Registro de usuarios nuevos.
- Inicio y cierre de sesión.
- Perfil con los datos del usuario y la lista de sus apuntes.
- Edición del perfil (nombre, apellido y email).

**Permisos**

- Cualquier visitante, aunque no haya iniciado sesión, puede ver el listado y el detalle de los apuntes.
- Crear apuntes, ver el perfil y editarlo requiere haber iniciado sesión. Si un visitante intenta entrar, se lo redirige al login.
- Solo el autor de un apunte puede editarlo o eliminarlo.
- La protección está en las vistas, con `LoginRequiredMixin` y `UserPassesTestMixin`.

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ceg1907/blog-apuntes.git
cd blog-apuntes
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

Activarlo:

- **Windows (CMD o PowerShell):** `venv\Scripts\activate`
- **Windows (Git Bash):** `source venv/Scripts/activate`
- **Mac o Linux:** `source venv/bin/activate`

Cuando está activo, aparece `(venv)` al principio de la línea de la terminal.

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

El proyecto lee la clave secreta y el modo de depuración desde un archivo `.env`, que no está en el repositorio por seguridad.

1. Copiar el archivo `.env.example` y renombrar la copia como `.env`.
2. Generar una clave secreta nueva:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. Pegar la clave generada en el `.env`. Debería quedar así:

   ```
   SECRET_KEY=la-clave-que-generaste
   DEBUG=True
   ```

`DEBUG=True` es necesario para que las imágenes se vean mientras se prueba el proyecto en modo desarrollo.

### 5. Aplicar las migraciones

Crea la base de datos y todas sus tablas:

```bash
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

Solo hace falta para entrar al panel de administración en `/admin/`:

```bash
python manage.py createsuperuser
```

Se pide un nombre de usuario, un email (opcional) y una contraseña. Mientras se escribe la contraseña no se ve nada en la pantalla: es normal.

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**

---

## Cómo probar el proyecto desde cero

El repositorio **no incluye** la base de datos (`db.sqlite3`) ni las imágenes subidas (`media/`), para que cada persona empiece con el proyecto limpio. Después de seguir los pasos de instalación, el blog arranca vacío. Para probarlo:

1. Entrar a **Registrarse** y crear un usuario. Al registrarse, se inicia sesión automáticamente.
2. Hacer clic en **Nuevo apunte** y crear uno **con imagen** y otro **sin imagen**. Se puede probar el formato Markdown, por ejemplo con `**negrita**` o un bloque de código entre tres comillas invertidas.
3. Abrir un apunte y probar los botones de **editar** (lápiz) y **eliminar** (tacho).
4. Dar **me gusta** a un apunte y volver a tocarlo para quitarlo.
5. Filtrar por categoría desde la barra lateral.
6. Entrar a **Mi perfil** y probar **Editar perfil**.
7. Cerrar sesión y comprobar que:
   - El listado y el detalle se siguen viendo.
   - Al intentar entrar a `/post/nuevo/` o a `/perfil/`, se redirige al login.

La carpeta `media/` se crea sola la primera vez que se sube una imagen.

---

## Rutas principales

| Ruta                   | Página                         | ¿Requiere sesión?  |
| ---------------------- | ------------------------------ | ------------------ |
| `/`                    | Listado de apuntes             | No                 |
| `/?categoria=python`   | Listado filtrado por categoría | No                 |
| `/post/<id>/`          | Detalle de un apunte           | No                 |
| `/post/nuevo/`         | Crear apunte                   | Sí                 |
| `/post/<id>/editar/`   | Editar apunte                  | Sí (solo el autor) |
| `/post/<id>/eliminar/` | Eliminar apunte                | Sí (solo el autor) |
| `/post/<id>/like/`     | Dar o quitar me gusta          | Sí                 |
| `/registro/`           | Registro                       | No                 |
| `/login/`              | Iniciar sesión                 | No                 |
| `/logout/`             | Cerrar sesión                  | Sí                 |
| `/perfil/`             | Mi perfil                      | Sí                 |
| `/perfil/editar/`      | Editar perfil                  | Sí                 |
| `/admin/`              | Panel de administración        | Superusuario       |

---

## Estructura del proyecto

```
blog-apuntes/
├── config/              # Configuración general del proyecto (settings, urls)
├── posts/               # App de apuntes: modelo, vistas, formularios y templates
├── usuarios/            # App de usuarios: registro, login, perfil
├── templates/           # Templates compartidos (base.html y partes reutilizables)
├── static/css/          # Estilos del sitio
├── .env.example         # Variables de entorno necesarias (sin valores reales)
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Autora

**Cristina Gonzalez** | [GitHub](https://github.com/ceg1907)
