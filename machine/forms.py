from django import forms
from .models import Machine


class MachineForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        machine = super().save(commit=False)
        if commit:
            machine.save()
        return machine

    class Meta:
        model = Machine
        fields = ['name', 'color']

