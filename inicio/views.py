from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from inicio.models import Blog
from inicio.forms import BlogForm , FormularioBusquedaBlogs



# Create your views here.


def inicio(request):
    return render(request, 'inicio/inicio.html' )




@login_required
def crear_blog(request):
    mensaje= ''
    
    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            blog = Blog(titulo=info['titulo'], subtitulo = info ['subtitulo'], autor = info ['autor'], fecha =info['fecha'], cuerpo = info ['cuerpo'], imagen = info ['imagen']) 
            
            blog.save()
            mensaje = f'Se creo el Blog {blog.titulo}'
        else:
            return render(request, 'inicio/crear_blog.html', {'formulario': formulario})
    
    formulario = BlogForm()
    return render(request, 'inicio/crear_blog.html', {'formulario': formulario, 'mensaje': mensaje})
    

@login_required
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs.html')  
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'modificar_blog.html', {'form': form, 'blog': blog})
    

def listar_blogs(request):
    formulario= FormularioBusquedaBlogs(request.GET)
    
    if formulario.is_valid():
        titulo_a_buscar= formulario.cleaned_data.get('titulo', '')
        lista_blogs =  Blog.objects.filter(titulo__icontains= titulo_a_buscar)
        
    formulario= FormularioBusquedaBlogs()
    return render(request, 'inicio/blogs.html', {'formulario':formulario, 'lista_blogs': lista_blogs})



class DetalleBlog(DetailView):
    model = Blog
   
    template_name = "inicio/detalle_blog.html"
    
    
class ModificarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['titulo','subtitulo', 'autor', 'fecha', 'cuerpo', 'imagen']
    template_name = "inicio/modificar_blog.html"
    success_url = reverse_lazy ('inicio:blogs')

class EliminarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "inicio/eliminar_blog.html"
    success_url = reverse_lazy ('inicio:blogs')
    

def acerca_de_mi(request):
    return render (request, 'inicio/acerca_de_mi.html')




