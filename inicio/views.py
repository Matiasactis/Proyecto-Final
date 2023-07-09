from django.shortcuts import render
from inicio.forms import CrearBlogForm
from inicio.models import Blog
# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html' )

def crear_blog(request):
    mensaje= ''
    
    if request.method == 'POST':
        formulario = CrearBlogForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog = Blog(nombre=info['nombre'], Autor =info['Autor'], Fecha =info['Fecha'],) 
            Blog.save()
            mensaje = f'Se creo el Blog {Blog.nombre}'
           

        
        else:
            return render(request, 'inicio/crear_blog.html', {'formulario': formulario})
    
    formulario = CrearBlogForm()
    return render(request, 'inicio/crear_blog.html', {'formulario': formulario, 'mensaje': mensaje})

