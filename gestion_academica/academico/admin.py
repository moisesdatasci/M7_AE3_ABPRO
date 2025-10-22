from django.contrib import admin
from .models import Profesor, Curso, Estudiante, Inscripcion, Perfil

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'email']
    search_fields = ['nombre', 'email']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'id_profesor']
    list_filter = ['id_profesor']
    search_fields = ['nombre']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'email']
    search_fields = ['nombre', 'email']

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['id_estudiante', 'id_curso', 'fecha_inscripcion', 'estado', 'nota_final']
    list_filter = ['estado', 'fecha_inscripcion']
    search_fields = ['id_estudiante__nombre', 'id_curso__nombre']

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id_estudiante', 'biografia']
    search_fields = ['id_estudiante__nombre']