


from enum import auto
from tabnanny import verbose
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Jugador(models.Model):
    
 
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    apodo = models.CharField(max_length=30,verbose_name='apodo')
    titulo_post = models.CharField(max_length=50, unique=False,null=True, verbose_name='Titulo')
    subtitulo_post= models.CharField(max_length=50,null=True,verbose_name='Subtitulo')
    contenido_post = RichTextField(null=True,blank=True,verbose_name='Contenido' )
    imagen_post = models.ImageField(upload_to='jugador',null=True,verbose_name='Imagen')
    fecha_jugador = models.DateTimeField(auto_now_add=True, )
    media_jugador = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.titulo_post
    class meta:
        db_table = 'jugador'
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = [id]

class Consola(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50, unique=False,null=True, verbose_name='Titulo')
    subtitulo = models.CharField(max_length=50,null=True,verbose_name='Subtitulo')
    contenido = RichTextField(null=True,blank=True,verbose_name='Contenido' )
    imagen_consola = models.ImageField(upload_to='consola',null=True,verbose_name='Imagen')
    fecha_consola = models.DateTimeField(auto_now_add=True,)
    media_consola = RichTextUploadingField(blank=True,null=True)
    
    
    def __str__(self):
        return self.titulo

    class meta:
        db_table = 'consola'
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'
        ordering = [id]


class Juegos(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    juego = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    titulo_posteo = models.CharField(max_length=50, unique=False,null=True, verbose_name='Titulo')
    subtitulo_posteo = models.CharField(max_length=50,null=True,verbose_name='Subtitulo')
    contenido_juego = RichTextField(null=True,blank=True,verbose_name='Contenido' )
    imagen_juego = models.ImageField(upload_to='juegos',null=True,verbose_name='Imagen')
    fecha_juego = models.DateTimeField(auto_now_add=True,)
    media_juego = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.titulo_posteo
    class meta:
        db_table = 'juego'
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        ordering = [id]



class Comentarios(models.Model):
    pass

