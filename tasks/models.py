from django.db import models
from django.contrib.auth.models import User # PAra poder relacionar los datos del user se importa este models
# Crear Modelos 


class Task(models.Model):
    title = models.CharField(max_length=100) # maximo de 100 caracteres
    descripction = models.TextField(blank=True) # textoslargos puede aceptar campos vacios
    created = models.DateTimeField(auto_now_add=True) # si no s ele pasa datos automaticmanete puede guardar la fecha 
    datecompleted = models.DateTimeField(null=True, blank=True ) # sera un campo vacio inicialmente , fecha que se realizo la tarea
    important = models.BooleanField(default=False) # Campo importante por defecto sera Falso ,el usuario puede marcarla importante 
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE si borra un campo borra todo. 
    
    def __str__(self):
        return self.title + '- by' + self.user.username #Para que retorna su propio titulotitulo
    
    
    
    # se debe ejecutar, Python mange.py makemigrations 
    # esto crea un model.py 
    # pyhton manage.py migrate
    # debemos importarlo a admin.py