# Generated by Django 4.2.3 on 2023-07-13 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='descripcion',
            new_name='cuerpo',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='nombre',
            new_name='subtitulo',
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='Titulo Predeterminado', max_length=15),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
