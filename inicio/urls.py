from django.urls import path
from inicio import views 

app_name= 'inicio'


urlpatterns = [
    path('', views.inicio, name='iniciacion'),
    path('blog/crear/', views.crear_blog, name= 'crear_blog'),
]
