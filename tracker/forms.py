from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags', 'is_done']
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DD HH:MM'},
                format='%Y-%m-%dT%H:%M'
            )
        }
