# 📓 Django Oficial Tutorial

Este es un proyecto introductorio para principiantes en Django que sigue la documentación oficial de Django.

A lo largo de este tutorial, te guiaremos por el proceso de creación de una aplicación básica para realizar encuestas que constará de 2 partes:

- Un sitio público que permite a los usuarios ver encuestas y votar en ellas.

- Un sitio de administración que permite añadir, modificar y eliminar encuestas.

## 🚀 Tecnologías utilizadas

- **Python 3.10+**
- **Django 5.2**
- SQLite (base de datos por defecto)
- HTML5, CSS3

## 🧱 Estructura del proyecto

```bash
.                                # Carpeta raíz del proyecto
├── LICENSE                      # Archivo de licencia del proyecto (MIT, GPL, etc.)
├── mysite/                      # Carpeta principal que contiene el proyecto Django y la app "polls"
│   ├── db.sqlite3               # Base de datos SQLite generada automáticamente por Django
│   ├── manage.py                 # Script para administrar el proyecto (migraciones, servidor, etc.)
│   ├── mysite/                   # Módulo del proyecto con la configuración principal de Django
│   │   ├── asgi.py               # Punto de entrada para ASGI (para despliegues asincrónicos)
│   │   ├── __init__.py           # Marca el directorio como un paquete de Python
│   │   ├── settings.py           # Configuración global del proyecto (BD, apps, rutas, etc.)
│   │   ├── urls.py               # Enrutador principal del proyecto
│   │   └── wsgi.py               # Punto de entrada para WSGI (para despliegues tradicionales)
│   └── polls/                    # Aplicación "polls" creada en el tutorial
│       ├── admin.py              # Configuración para registrar modelos en el panel de administración
│       ├── apps.py               # Configuración de la app (nombre, etiquetas, etc.)
│       ├── __init__.py           # Marca el directorio como un paquete de Python
│       ├── migrations/           # Carpeta que contiene migraciones de base de datos
│       │   ├── 0001_initial.py   # Primera migración creada (estructura inicial de tablas)
│       │   └── __init__.py       # Marca la carpeta como un paquete Python
│       ├── models.py             # Definición de modelos (tablas y relaciones de la BD)
│       ├── static/               # Archivos estáticos de la app
│       │   └── polls/            # Carpeta específica para la app "polls"
│       │       ├── images/       # Imágenes utilizadas en la app
│       │       │   └── python-background.jpg  # Imagen de fondo para la app
│       │       └── style.css     # Estilos CSS de la app
│       ├── templates/            # Plantillas HTML específicas de la app
│       │   └── polls/            # Carpeta con plantillas de "polls"
│       │       ├── detail.html   # Página de detalle de una encuesta
│       │       ├── index.html    # Página principal que lista encuestas
│       │       └── results.html  # Página que muestra resultados de una encuesta
│       ├── tests.py              # Pruebas unitarias de la app
│       ├── urls.py               # Enrutador específico de la app "polls"
│       └── views.py              # Vistas que manejan la lógica de las solicitudes HTTP
├── README.md                     # Descripción general del proyecto y cómo ejecutarlo
├── requirements.txt              # Lista de dependencias del proyecto (para instalación rápida)
└── templates/                    # Plantillas HTML globales del proyecto
    └── admin/                    # Plantillas personalizadas del panel de administración de Django
        ├── base_site.html        # Plantilla base modificada del admin
        └── index.html            # Página principal personalizada del admin

```

### 🔄 Operaciones CRUD

#### Polls App

| **Method** | **URL**                            | **Action**                                      |
|------------|------------------------------------|-------------------------------------------------|
| GET        | `/polls`                           | Retrive all Questions                           |
| GET        | `/polls/sepecifics/:id`            | Find a Question By Id                           |
| POST       | `/polls/sepecifics/:id`            | Vote a Choice in a Question by `:id`            |
| GET        | `/polls/sepecifics/:id/results`    | View votes results in a Question by `:id`       |

#### Admin App

| **Method** | **URL**                            | **Action**                                      |
|------------|------------------------------------|-------------------------------------------------|
| POST       | `/admin/login`                     | Log in whit a Superuser                         |
| GET        | `/admin`                           | Retrieve All Apps and Models                    |
| GET        | `/admin/polls/question`            | Retrive all Questions                           |
| CREATE     | `/admin/polls/question/add`        | Create a new Question                           |
| DELETE     | `/admin/polls/question`            | Delete selected Questions                       |
| PUT        | `/admin/polls/question/:id/change` | Update a question by `:id`                      |
| DELETE     | `/admin/polls/question/:id/change` | Delete a question by `:id`                      |
| GET        | `/admin/polls/choice`              | Retrive all Choices                             |
| CREATE     | `/admin/polls/choice/add`          | Create a new Choices                            |
| DELETE     | `/admin/polls/choice`              | Delete selected Choices                         |
| PUT        | `/admin/polls/choice/:id/change`   | Update a Choice by `:id`                        |
| DELETE     | `/admin/polls/choice/:id/change`   | Delete a Choice by `:id`                        |

## 👨‍💻 Autor

**ancu-98**

- 💼 [LinkedIn](https://www.linkedin.com/in/ancu98)
- 🐦 [X (Twitter)](https://x.com/)
- 🌐 [Portfolio Web](https://ancu98-website.netlify.app/#)

## ⚙️ Instalación

### 📌 Requisitos del Sistema

Para ejecutar correctamente este proyecto necesitas tener instalado lo siguiente en tu sistema:

| Requisito     | Descripción                                    |
| ------------- | -----------------------------------------------|
| Python 3.10+  | Recomendado `v3.12.3`, con `venv` habilitado   |
| pip           | Administrador de paquetes de Python            |
| Virtualenv    | Opcional, pero recomendado para aislar entornos|
| Git           | Para clonar el repositorio                     |
| Navegador web | Para acceder a la aplicación Django            |


### 1. CLonar el repositorio

```bash
git clone https://github.com/ancu-98/Django_Official_Tutorial.git
cd Django_Official_Tutorial
```

### 2. Instala Django

🐧 En Linux/macOS:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cd mysite
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
🪟 En Windows (CMD o PowerShell):

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
cd mysite
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
> *Una vez tengas corriendo Django, accede a http://127.0.0.1:8000 desde el navegador*

## 📚 Documentación paso a paso

Aquí te muestro la documentación del paso a paso de cómo construí el proyecto, por si quieres crear este proyecto tu mismo desde cero:

📄[Step by step Docs](https://www.notion.so/Django-Theory-2333afe76d7180ba812cc694b004ee7d?source=copy_link)

> Si bién es el seguimiento de exactamente la documentación que ofrece Django, agrego pasos e items adicionales que permiten entender e ilustrar mejor el paso a paso del tutorial.

## 🎓 Bonus
Si quieres entender un poco más a fondo **cómo Django procesa una solicitud desde que llega al servidor hasta que retorna una respuesta al navegador**, puedes consultar el archivo:

📁[`ancu-98/React_Django_CRUD/Server/README.md`](https://github.com/ancu-98/React_Django_CRUD/blob/main/Server/README.md)

> Una lectura recomendada si quieres entender cómo Django opera “por dentro”.

## 📩 Contratación
Si deseas colaborar o contratar servicios de desarrollo en Django, puedes escribirme a: ancu_inbox@hotmail.com para consultas.

## 🔐 Licencia

Este proyecto se distribuye bajo los términos de la [Licencia MIT](./LICENSE).

El código base de la aplicación **polls** proviene de la documentación oficial de [Django](https://docs.djangoproject.com/) y es propiedad de sus respectivos autores y colaboradores.

Las modificaciones, adaptaciones y mejoras realizadas sobre dicho código están cubiertas por la Licencia MIT incluida en este repositorio.

¿Te gustó este repo? ¡Dale ⭐ en GitHub y compártelo con tu equipo!

