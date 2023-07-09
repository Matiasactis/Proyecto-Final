from django import forms

class CrearBlogForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    autor = forms.CharField(max_length=20)
    fecha = forms.DateField()
    # descripcion = RichTextField()
    