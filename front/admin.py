from django.contrib import admin
from .models import Publicacion, Logo, Notificacion, Requisito, Beneficio

# Register your models here.
class InlineRequisito(admin.TabularInline):
    model = Requisito
    extra = 0

class PublicacionInline(admin.TabularInline):
    model = Publicacion
    fields = ('titulo', 'contenido', 'imagen', 'estado', 'eliminado')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    extra = 0

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'puesto', 'estado')
    search_fields = ('titulo', 'empresa', 'puesto', 'estado')
    date_hierarchy = 'fecha_modificacion'
    list_filter = ('fecha_creacion', 'fecha_modificacion')
    
    
    
    

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('user', 'titulo_publicacion','url_publicacion', 'estado')
    search_fields = ('user', 'titulo_publicacion', 'estado')
    date_hierarchy = 'fecha_modificacion'
    list_filter = ('fecha_creacion', 'fecha_modificacion')
    
    def save_model(self, request, obj, form, change):
        if 'estado' in form.changed_data:
            obj.publicacion.estado = 'activo'
            obj.publicacion.save()
        super().save_model(request, obj, form, change)


    

admin.site.register(Logo)
admin.site.register(Notificacion, NotificacionAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Requisito)
admin.site.register(Beneficio)