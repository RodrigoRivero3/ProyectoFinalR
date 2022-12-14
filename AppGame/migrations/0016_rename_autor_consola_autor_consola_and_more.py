# Generated by Django 4.1 on 2022-09-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0015_alter_consola_imagen_alter_juegos_imagen_juego_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consola',
            old_name='autor',
            new_name='autor_consola',
        ),
        migrations.RenameField(
            model_name='consola',
            old_name='publicado',
            new_name='fecha_consola',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='autor',
            new_name='autor_juegos',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='publicado',
            new_name='fecha_juego',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='autor',
            new_name='autor_jugador',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='publicado',
            new_name='fecha_jugador',
        ),
    ]
