from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name= 'usuario'


urlpatterns = [
    path('Login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name= 'usuario/logout.html'),  name='logout'),
    path('registro/', views.registrarse, name = 'registrarse'),
    path('perfil/editar/', views.edicion_perfil , name = 'editar_perfil'),
    path('perfil/editar/contrasenia/', views.ModificarContra.as_view() , name = 'cambiar_contra'),
    
    # path('Usuario/Detalles', 'usuario/usuario.html', name = 'usuario')
    
]
