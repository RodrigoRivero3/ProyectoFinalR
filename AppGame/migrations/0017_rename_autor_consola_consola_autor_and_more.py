# Generated by Django 4.1 on 2022-09-30 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0016_rename_autor_consola_autor_consola_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consola',
            old_name='autor_consola',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='juegos',
            old_name='autor_juegos',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='autor_jugador',
            new_name='autor',
        ),
    ]
