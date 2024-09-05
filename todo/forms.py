from django import forms
from .models import CreateTask
class CreateTaskModelForm(forms.ModelForm):
    class Meta:
        model = CreateTask
        fields = [
            'article',
            'image',
            'body',
            'status'
        ]