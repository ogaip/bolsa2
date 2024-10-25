from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from account.views import login_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('eliminacion_definitiva/<int:id>/', views.eliminar_definitivamente, name='eliminacion_definitiva'),
    path('ver/<int:id>/', views.ver, name='ver'),
    path('admin/', views.admin, name='admin'),
    path('api/data', views.get_dataPublicaciones, name='jsondata'),
    path('charts/', views.charts, name='charts'),
    path('rePublicar/<int:id>/', views.solicitar_publicacion, name='rePublicar'),
    path('modoAdmin/<int:id>', views.modo_admin, name='modo_admin'),
    path('editarAdmin/<int:id>', views.editar_admin, name='editar_admin'),
    
    path('admin_noti/', views.admin_notificaciones, name='admin_notificaciones'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)