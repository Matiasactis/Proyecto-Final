from django.urls import path
from inicio import views 

app_name= 'inicio'


urlpatterns = [
    path('', views.inicio, name='iniciacion'),
    path('acercademi/', views.acerca_de_mi , name ='acerca_de_mi') ,
    path('blog/crear/', views.crear_blog, name= 'crear_blog'),
    path('blogs/', views.listar_blogs, name= 'blogs'),
    path('blogs/<int:pk>/', views.DetalleBlog.as_view() , name= 'detalle_blog'),
    path('blogs/<int:pk>/modificar/', views.ModificarBlog.as_view(), name= 'modificar_blog'),
    path('blogs/<int:pk>/eliminar/', views.EliminarBlog.as_view(), name= 'eliminar_blog'),
]
