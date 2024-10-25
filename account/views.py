from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Perfil
from front.views import get_logo
from .forms import EditPerfilForm, EditUserForm

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login/login.html')
        
    
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.create_user(username, email, password)
        perfil = Perfil.objects.create(user=user.id)
        if user:
            login(request, user)
            return render(request, 'login/login.html', {'message': 'Usuario creado correctamente'})
        else:
            return render(request, 'login/register.html', {'error': 'No se pudo crear el usuario'})
    else:
        return render(request, 'login/register.html')


    

############### Account  ####################
@login_required
def perfil(request, id):
    user = request.user
    fuser= User.objects.filter(username=user.username).values()
    perfil = get_object_or_404(Perfil, user=user.id)
    logo = get_logo(request)

    print(perfil)
    return render(request, 'account/perfil.html', {
        'user': user,
        'fuser': fuser,
        'perfil': perfil,
        'logo': logo,
        })

def editar_perfil(request, id):
    user = request.user
    fuser = User.objects.filter(username=user).values()
    perfil = get_object_or_404(Perfil, user=user.id)
    logo = get_logo(request)
    form = EditPerfilForm(instance=perfil)

    if request.method == 'POST':
        form = EditPerfilForm(request.POST, request.FILES, instance=perfil)
        
        if form.is_valid():
            form.save()
            return redirect('perfil', id=user.id)
        else:
            form = EditPerfilForm(instance=perfil)

    return render(request, 'account/editar_perfil.html', {
        'user': user,
        'fuser': fuser,
        'perfil': perfil,
        'logo': logo,
        'form': form,
    })


