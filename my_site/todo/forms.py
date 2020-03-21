from django import forms
from . import models

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        exclude = ('project',)


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        exclude = ('account',)
        

        

        
