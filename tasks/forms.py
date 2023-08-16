from django import forms

from .models import Tasks


class AddNewTaskForm(forms.ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Название',
        'maxlength': '32'
    }))

    short_description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Краткое описание',
        'maxlength': '128'
    }))

    class Meta:
        model = Tasks
        fields = ('task', 'short_description')


class EditTaskForm(AddNewTaskForm):
    stage = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'select-css'
    }), choices=Tasks.STAGE_CHOICE)

    class Meta:
        model = Tasks
        fields = ('task', 'short_description', 'stage')
