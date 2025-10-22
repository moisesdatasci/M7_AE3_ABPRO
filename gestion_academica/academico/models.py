from django.db import models

# Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return self.nombre


# Modelo Curso - Uno a muchos
class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    # ForeignKey: Un profesor puede tener muchos cursos
    # on_delete=models.CASCADE: Si se borra el profesor, se borran sus cursos
    id_profesor = models.ForeignKey(
        Profesor, 
        on_delete=models.CASCADE, 
        related_name='cursos'
    )
    
    def __str__(self):
        return self.nombre


# Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre


# Modelo Inscripcion - Muchos a muchos
class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('FINALIZADO', 'Finalizado'),
    ]
    
    id_estudiante = models.ForeignKey(
        Estudiante, 
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    id_curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=10, 
        choices=ESTADO_CHOICES, 
        default='ACTIVO'
    )
    nota_final = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    
    class Meta:
        unique_together = ['id_estudiante', 'id_curso']
        verbose_name_plural = "Inscripciones"
    
    def __str__(self):
        return f"{self.id_estudiante.nombre} - {self.id_curso.nombre}"


# Modelo Perfil - relacion uno a uno
class Perfil(models.Model):
    id_estudiante = models.OneToOneField(
        Estudiante, 
        on_delete=models.CASCADE,
        related_name='perfil',
        primary_key=True
    )
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    redes = models.JSONField(default=dict, blank=True) 
    
    class Meta:
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"Perfil de {self.id_estudiante.nombre}"