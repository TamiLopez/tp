from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    
    class Meta:
        model = Task # le indicamos que proviene de este Molde y lo importamos
        fields = ["title", 'description', 'important']