from django import forms
from app.models import *

class Student(forms.Form):
    name=forms.CharField(max_length=33)
    age=forms.IntegerField(max_value=100)


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'