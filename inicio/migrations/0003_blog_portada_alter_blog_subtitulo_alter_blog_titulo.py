# Generated by Django 4.2.2 on 2023-07-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_descripcion_blog_cuerpo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='Titulo Predeterminado', max_length=30),
        ),
    ]
