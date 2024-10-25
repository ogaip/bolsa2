from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Perfil

# Register your models here.

class InlinePerfil(admin.TabularInline):
    model = Perfil
    extra = 0
    
    

class PerfilAdmin(admin.ModelAdmin):
    inlines = [InlinePerfil,]
    list_display = ('username', 'email', 'first_name','last_name', 'is_staff', 'is_active')
    
    


admin.site.unregister(User)

admin.site.register(Perfil)

admin.site.register(User, PerfilAdmin)


