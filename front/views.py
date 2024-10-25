from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Logo, Notificacion
from account.models import Perfil
from .forms import PublicacionForm, PublicacionFormModeAdmin
from django.contrib.auth.models import User
############### metricas  ####################
from django.db.models import Count
from datetime import datetime, timedelta
from django.http import JsonResponse
import random



# Create your views here.

def notificaciones(request):
    if request.user.is_staff:
        noticaciones = Notificacion.objects.filter(estado='pendiente').values().order_by('-fecha_creacion')
        noti= noticaciones
        return noti
    else:
        return "No es Admin"
        
    

@login_required
def get_logo(request):
    logos = Logo.objects.all()
    return logos.first() if logos.exists() else None

def metricas_publicaciones(request):
    hoy = datetime.now().date()
    una_semana_atras = hoy - timedelta(days=7)
    
    publicaciones_por_fecha = (
        Publicacion.objects.filter(fecha_creacion__range=[una_semana_atras, hoy]).values('fecha_creacion').annotate(count=Count('id')).order_by('fecha_creacion')
    )
    
    fechas = [pub['fecha_creacion'] for pub in publicaciones_por_fecha]
    conteo = [pub['count'] for pub in publicaciones_por_fecha]
    
    return {
        'fechas': fechas,
        'conteo': conteo,
    }
    
    

@login_required
def admin(request):
    redirect('admin/')
@login_required
def admin_notificaciones(request):
    url = '/admin/front/notificacion/'
    return redirect(f'{url}')

def index(request):
    if request.user.is_authenticated:
        
        user=request.user
        perfil = get_object_or_404(Perfil, user=user.id)
        fuser = User.objects.filter(username=user).values()
        metri = metricas_publicaciones(request)
        logo = get_logo(request)
        if request.user.is_staff:
            noti= notificaciones(request)
            return render(request, 'pages/index.html', {
                'user': user,
                'fuser': fuser,
                'perfil': perfil,
                'logo': logo,
                'noti': noti,
                })
        else:
            return render(request, 'pages/index.html', {
                'user': user,
                'fuser': fuser,
                'perfil': perfil,
                'logo': logo,
                'metri': metri,
            })
    else:
        print("no es autenticado")
        return render(request, 'login/login.html')
        

        
@login_required
def listar(request):
    
    if request.user.is_staff:
        publicaciones_activas = Publicacion.objects.filter(estado='activo').values().order_by('-fecha_modificacion')
        publicaciones_inactivas = Publicacion.objects.filter(estado='inactivo').values().order_by('-fecha_modificacion')
        user = request.user
        perfil = get_object_or_404(Perfil, pk=user.id)
        fuser = User.objects.filter(username=user).values()
        logo = get_logo(request)
        
        return render(request, 'pages/publicaciones/listar.html', {
            'publicaciones_activas': publicaciones_activas,
            'publicaciones_inactivas': publicaciones_inactivas,
            'perfil': perfil,
            'logo': logo,
            'fuser': fuser,
            })
    else:    
        user = request.user
        perfil = get_object_or_404(Perfil, pk=user.id)
        fuser = User.objects.filter(username=user).values()
        publicaciones_activas = Publicacion.objects.filter(user=user.id, estado='activo').values().order_by('-fecha_modificacion')
        publicaciones_inactivas = Publicacion.objects.filter(user=user.id, estado='inactivo').values().order_by('-fecha_modificacion')
        logo = get_logo(request)
        return render(request, 'pages/publicaciones/listar.html', {
            'publicaciones_activas': publicaciones_activas,
            'publicaciones_inactivas': publicaciones_inactivas,
            'perfil': perfil,
            'logo': logo,
            'fuser': fuser,
            })

@login_required
def crear(request):
    user = request.user
    perfil = get_object_or_404(Perfil, pk=user.id)
    form = PublicacionForm()
    logo = get_logo(request)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            Publicacion.objects.create(user=request.user, titulo=form.cleaned_data['titulo'], contenido=form.cleaned_data['contenido'], imagen=form.cleaned_data['imagen'])
            
            return redirect('listar')
    else:
        form = PublicacionForm()
    return render(request, 'pages/publicaciones/crear.html', {
        'form': form,
        'perfil': perfil,
        'logo': logo,
        })

@login_required
def editar(request, id):
    user = request.user
    perfil = get_object_or_404(Perfil , pk=user.id)
    logo = get_logo(request)
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=id)
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        publicacion = Publicacion.objects.get(id=id)
        form = PublicacionForm(instance=publicacion)
        return render(request, 'pages/publicaciones/editar.html', {
            'form': form,
            'perfil': perfil,
            'logo': logo,
            })

def editar_admin(request, id):
    user = request.user
    perfil = get_object_or_404(Perfil , pk=user.id)
    logo = get_logo(request)
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=id)
        form = PublicacionFormModeAdmin(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            
            return redirect('listar')
    else:
        publicacion = Publicacion.objects.get(id=id)
        form = PublicacionForm(instance=publicacion)
        return render(request, 'pages/publicaciones/editar.html', {
            'form': form,
            'perfil': perfil,
            'logo': logo,
            })
    
@login_required
def eliminar(request, id):
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=id)
        publicacion.estado= 'inactivo'
        publicacion.save()
        return redirect('listar')
    else:
        return redirect('listar')

@login_required
def eliminar_definitivamente(request, id):
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=id)
        publicacion.eliminado = True
        publicacion.save()
        
        return redirect('listar')
    else:
        return redirect('listar')
    
@login_required
def ver(request, id):
    user = request.user
    is_staff = user.is_staff
    print(is_staff)
    perfil = get_object_or_404(Perfil, pk=user.id)
    ver = Publicacion.objects.get(id=id)
    logo = get_logo(request)
    return render(request, 'pages/publicaciones/ver.html', {
        'publicacion': ver,
        'perfil': perfil,
        'logo': logo,
        'is_staff': is_staff,
        })
    
def generar_color_aleratorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b}, 0.5)'

def get_dataPublicaciones(request):
    Publicaciones = Publicacion.objects.all()
    colores = [generar_color_aleratorio() for _ in Publicaciones]
    data = {
        'labels': [publicacion.titulo for publicacion in Publicaciones],
        'datasets': [{
            'label': 'Publicaciones',
            'data': [publicacion.id for publicacion in Publicaciones],
            'backgroundColor': colores,
            'borderColor': colores,
            'borderWidth': 1,    
        }],
        
    }
    return JsonResponse(data)

def charts(request):
    user = request.user
    perfil = get_object_or_404(Perfil, pk=user.id)
    logo = get_logo(request)
    
   
    
    
    return render(request, 'pages/charts/chartjs.html', {
        'perfil': perfil,
        'logo': logo,
        })
    
def solicitar_publicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    url = f'http://127.0.0.1:8000/ver/{publicacion.id}/'
    notificacion = Notificacion.objects.create(user=publicacion.user, titulo_publicacion=publicacion.titulo, url_publicacion=url ,estado='pendiente', publicacion_id=publicacion.id) 
    mensaje = f'Se ha solicitado la publicación de {publicacion.titulo}'
    return redirect('listar')

def modo_admin(request, id):
    user = request.user
    perfil = get_object_or_404(Perfil, pk=user.id)
    fuser = User.objects.filter(username=user).values()
    publicacion = Publicacion.objects.get(id=id)
    
    print(publicacion)
    form = PublicacionFormModeAdmin(instance=publicacion)
    logo = get_logo(request)
    
    
    return render(request, 'pages/admin/editar_publicacion.html', {
        'user': user,
        'fuser': fuser,
        'perfil': perfil,
        'logo': logo,
        'form': form,
        'publicacion': publicacion,        
        })

