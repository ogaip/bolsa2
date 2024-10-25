from django.db import models

# Create your models here.
class Publicacion(models.Model):
    ESTADO = (
        ('activo', 'Publicado'),
        ('inactivo', 'No publicado'),
    )
    HORARIO_CHOICES = (
        ('Lunes a Viernes', 'Lunes a Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo'),
        ('Lunes a Sabado', 'Lunes a Sabado'),
        ('Lunes a Domingo', 'Lunes a Domingo'),
    )
    
    MODALIDAD_CHOICES = (
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Mixto', 'Mixto'),
    )
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    horario = models.CharField(max_length=100, choices=HORARIO_CHOICES, default='Lunes a Viernes')
    modalidad = models.CharField(max_length=100, choices=MODALIDAD_CHOICES, default='Presencial')
    salario = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True, default=2000)
    tareas = models.TextField()
    imagen = models.ImageField(upload_to='publicaciones', null=True, blank=True)
    estado = models.CharField(max_length=50, choices=ESTADO, default='activo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    re_requisitos = models.ManyToManyField('Requisito', related_name='publicaciones')
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        db_table = 'publicaciones'
        

class Requisito(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nombre
    
    
    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        db_table = 'requisitos'

class Beneficio(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'
        db_table = 'beneficios'

class Logo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'
        db_table = 'logos'

class Notificacion(models.Model):
    ESTADO_NOTIFICACION = (
        ('pendiente', 'Pendiente'),
        ('realizado', 'Realizado'),
    )    
    user = models.CharField(max_length=100)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='notificaciones')
    titulo_publicacion = models.CharField(max_length=100)
    url_publicacion = models.URLField(max_length=200)
    estado = models.CharField(max_length=50, choices=ESTADO_NOTIFICACION, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Notificacion para {self.publicacion.titulo}'
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        db_table = 'notificaciones'