from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created") # creamos una clase para que pueda mostrarnos tareas
    # admin.site.rester(Task, TaskAdmin)

# Register your models here.
admin.site.register(Task, TaskAdmin) # se gere cuando se guarda y se ejecute el servidor
