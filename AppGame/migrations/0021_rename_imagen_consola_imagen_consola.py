# Generated by Django 4.1 on 2022-10-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0020_alter_consola_titulo_alter_juegos_titulo_posteo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consola',
            old_name='imagen',
            new_name='imagen_consola',
        ),
    ]