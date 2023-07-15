from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuario.form import FormularioCreacionUsuario, FormEditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuario.models import Infoextra



# Create your views here.

def login(request):
    
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data =request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contra = formulario.cleaned_data['password']
            
            user = authenticate(username= usuario, password= contra )
            
            django_login(request, user)
            
            
            Infoextra.objects.get_or_create(user = user)
            return redirect('inicio:iniciacion')
            
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
                
        
            
    
    formulario = AuthenticationForm()
    
    return render(request, 'usuario/login.html', {'formulario': formulario})


def registrarse(request):
    
    if request.method == 'POST':
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render (request, 'usuario/registro.html', {'formulario': formulario})
    
    formulario = FormularioCreacionUsuario()
    return render (request, 'usuario/registro.html', {'formulario': formulario})


@login_required
def edicion_perfil(request):
    
    info_extra_user= request.user.infoextra
    
    
    
    if request.method == 'POST':
        formulario = FormEditarPerfil (request.POST, request.FILES,  instance = request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
            
                info_extra_user.avatar = avatar
            
                info_extra_user.save()
            
            formulario.save()
            
            
            return redirect ('inicio:iniciacion')
            
        else:
            return render (request, 'usuario/edicion_perfil.html', {'formulario': formulario})
    
    else:
        formulario = FormEditarPerfil(initial = {'avatar': info_extra_user.avatar},  instance = request.user)
    return render (request, 'usuario/edicion_perfil.html', {'formulario': formulario})



class ModificarContra(LoginRequiredMixin,PasswordChangeView):
     template_name = 'usuario/edicion_contra.html'
     success_url = reverse_lazy ('usuario:edicion_perfil')