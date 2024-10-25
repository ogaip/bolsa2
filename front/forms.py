from django.forms import ModelForm
from .models import Publicacion

class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'empresa', 'puesto', 'horario', 'modalidad', 'salario', 'tareas', 'imagen']
        labels = {
            'titulo': 'Titulo',
            'empresa': 'Empresa',
            'puesto': 'Puesto',
            'horario': 'Horario',
            'modalidad': 'Modalidad',
            'salario': 'Salario',
            'tareas': 'Tareas',
            'imagen': 'Imagen',
        }
        
class PublicacionFormModeAdmin(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'empresa', 'puesto', 'horario', 'modalidad', 'salario', 'tareas', 'imagen', 'estado']
        labels = {
            'titulo': 'Titulo',
            'empresa': 'Empresa',
            'puesto': 'Puesto',
            'horario': 'Horario',
            'modalidad': 'Modalidad',
            'salario': 'Salario',
            'tareas': 'Tareas',
            'imagen': 'Imagen',
            'estado': 'Estado',
        }
        
        