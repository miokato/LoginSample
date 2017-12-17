from django import forms
from .models import Workshop


class WorkshopForm(forms.ModelForm):
    title = forms.CharField(label='タイトル', required=True)
    detail = forms.Textarea()
    do_date = forms.DateField(label='開催日', required=True)
    used_machine = forms.CheckboxInput()
    duration_time = forms.DurationField(label='開催時間', required=True)
    requirements = forms.CharField(label='持ち物', required=True)

    class Meta:
        model = Workshop
        fields = ['title', 'detail', 'do_date', 'used_machine', 'duration_time', 'requirements']

    def save(self, commit=True):
        case = super(WorkshopForm, self).save(commit=False)
        if commit:
            case.save()
        return case

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['detail'].widget.attrs['class'] = 'form-control'
        self.fields['do_date'].widget.attrs['class'] = 'form-control'
        self.fields['used_machine'].widget.attrs['class'] = 'form-control'
        self.fields['duration_time'].widget.attrs['class'] = 'form-control'
        self.fields['requirements'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'レーザー講習会'
        self.fields['detail'].widget.attrs['placeholder'] = 'レーザー加工機を使った講習会です。'
        self.fields['do_date'].widget.attrs['placeholder'] = '2017-10-22'
        self.fields['used_machine'].widget.attrs['placeholder'] = '3D'
        self.fields['requirements'].widget.attrs['placeholder'] = 'ノートPC'
