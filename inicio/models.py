from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class Blog (models.Model):
    titulo = models.CharField(max_length=30, default='Titulo Predeterminado')
    subtitulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    fecha = models.DateField(default= timezone.now)
    cuerpo = RichTextField()
    imagen = models.ImageField(upload_to='blog_images/', blank= True  ,null=True)
    
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Subtitulo:{self.subtitulo} - Autor {self.autor} - Fecha {self.fecha} - Cuerpo: {self.cuerpo} Imagen: {self.imagen}'
    
    