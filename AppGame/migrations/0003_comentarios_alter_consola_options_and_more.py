# Generated by Django 4.1 on 2022-09-27 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppGame', '0002_alter_jugador_apodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='consola',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AlterModelOptions(
            name='juegos',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AlterModelOptions(
            name='jugador',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AlterModelManagers(
            name='consola',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='juegos',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='jugador',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='consola',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consola',
            name='contenido',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='consola',
            name='estado',
            field=models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10),
        ),
        migrations.AddField(
            model_name='consola',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='consola',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='consola',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, unique_for_date='publicado'),
        ),
        migrations.AddField(
            model_name='consola',
            name='subtitulo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='consola',
            name='titulo',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='juegos',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='juegos',
            name='contenido',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='juegos',
            name='estado',
            field=models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10),
        ),
        migrations.AddField(
            model_name='juegos',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='juegos',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='juegos',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, unique_for_date='publicado'),
        ),
        migrations.AddField(
            model_name='juegos',
            name='subtitulo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='juegos',
            name='titulo',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jugador',
            name='contenido',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='estado',
            field=models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10),
        ),
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='jugador',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='jugador',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, unique_for_date='publicado'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='subtitulo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='titulo',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='apodo',
            field=models.CharField(max_length=30),
        ),
    ]
