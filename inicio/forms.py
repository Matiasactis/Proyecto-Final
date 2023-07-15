from django import forms
from django.utils import timezone
from ckeditor.fields import RichTextFormField

class CrearBlogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(required= False)
    autor = forms.CharField(max_length=20)
    fecha = forms.DateField()
    cuerpo = RichTextFormField()
    
    
    
class FormularioBusquedaBlogs(forms.Form):
    titulo = forms.CharField(max_length=20, required= False )
    