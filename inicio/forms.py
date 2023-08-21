from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextFormField
from inicio.models import Blog

#class CrearBlogForm(forms.Form):
 #   titulo = forms.CharField(max_length=50)
  #  subtitulo = forms.CharField(required= False)
   # autor = forms.CharField(max_length=20)
    #fecha = forms.DateField()
    #cuerpo = RichTextFormField()
    


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo','cuerpo','autor','fecha','imagen']

    
    
    
class FormularioBusquedaBlogs(forms.Form):
    titulo = forms.CharField(max_length=20, required= False )
    