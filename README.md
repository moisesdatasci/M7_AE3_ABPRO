# 🎓 Sistema de Gestión Académica

Sistema de gestión académica desarrollado con Django para administrar profesores, cursos, estudiantes e inscripciones.

## 📋 Descripción

Plataforma educativa que permite:
- Gestión de profesores y cursos
- Inscripción de estudiantes en múltiples cursos
- Seguimiento de notas y estados de inscripción
- Perfiles personalizados para estudiantes

## 🗄️ Modelo de Datos

El sistema implementa las siguientes relaciones:

- **Muchos a Uno**: Un profesor puede impartir varios cursos
- **Muchos a Muchos**: Estudiantes pueden inscribirse en múltiples cursos (con tabla intermedia)
- **Uno a Uno**: Cada estudiante tiene un perfil único

## 🚀 Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/moisesdatasci/M7_AE3_ABPRO
cd gestion-academica
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
```bash
# Windows
venv\Scripts\activate

```

4. **Instalar dependencias**
```bash
pip install django pillow
```

5. **Crear migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario** (opcional)
```bash
python manage.py createsuperuser
```

7. **Iniciar servidor**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
- Aplicación: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin

## 📦 Modelos

### Profesor
- nombre
- email

### Curso
- nombre
- descripción
- id_profesor (ForeignKey)

### Estudiante
- nombre
- email

### Inscripcion
- id_estudiante (ForeignKey)
- id_curso (ForeignKey)
- fecha_inscripcion
- estado (Activo/Finalizado)
- nota_final

### Perfil
- id_estudiante (OneToOneField)
- biografía
- foto
- redes sociales

## 🧪 Pruebas en Consola

Para probar el sistema, abre la consola de Django:

```bash
python manage.py shell
```

Luego ejecuta:

```python
from academico.models import Profesor, Curso, Estudiante, Inscripcion, Perfil

# Crear un profesor
profesor = Profesor.objects.create(
    nombre="Leik Caro",
    email="leik.caron@skillnet.edu"
)

# Crear un curso
curso = Curso.objects.create(
    nombre="Python Avanzado",
    descripcion="Curso de programación avanzada",
    id_profesor=profesor
)

# Crear estudiante
estudiante = Estudiante.objects.create(
    nombre="Moisés Ortega",
    email="moises.ortega@skillnet.edu"
)

# Inscribir estudiante
inscripcion = Inscripcion.objects.create(
    id_estudiante=estudiante,
    id_curso=curso,
    estado='ACTIVO'
)

# Crear perfil
perfil = Perfil.objects.create(
    id_estudiante=estudiante,
    biografia="Estudiante apasionada por la tecnología",
    redes={"github": "github.com/moisesdatasci"}
)
```

Para salir de la consola:
```python
exit()
```

## 📁 Estructura del Proyecto

```
gestion_academica/
│
├── gestion_academica/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── academico/                  # Aplicación principal
│   ├── models.py              # Modelos de datos
│   ├── admin.py               # Configuración del admin
│   ├── views.py
│   └── migrations/
│
├── manage.py
└── requirements.txt
```

## 🛠️ Tecnologías

- **Django 5.1+**: Framework web
- **SQLite**: Base de datos (por defecto)
- **Pillow**: Manejo de imágenes

## 👥 Características

✅ CRUD completo de profesores, cursos y estudiantes  
✅ Sistema de inscripciones con estados y notas  
✅ Perfiles personalizados con redes sociales  
✅ Panel de administración de Django  
✅ Borrado en cascada automático  
✅ Validación de inscripciones únicas  

## 👨‍💻 Autor

Tu Nombre - [GitHub](https://github.com/moisesdatasci)



---

⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub!
