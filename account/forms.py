from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class EditPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        
        
        
        