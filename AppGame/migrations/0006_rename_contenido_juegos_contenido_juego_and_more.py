# Generated by Django 4.1 on 2022-09-28 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0005_rename_contenido_jugador_contenido_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juegos',
            old_name='contenido',
            new_name='contenido_juego',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='imagen',
            new_name='imagen_juego',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='nombre',
            new_name='juego',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='subtitulo',
            new_name='subtitulo_posteo',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='titulo',
            new_name='titulo_posteo',
        ),
    ]
