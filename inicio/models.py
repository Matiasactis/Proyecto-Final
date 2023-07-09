from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog (models.Model):
    nombre = models.CharField(max_length=15)
    autor = models.CharField(max_length=20)
    fecha = models.DateField()
    descripcion = RichTextField()
    
    