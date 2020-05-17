from django import forms
from home.models import Profile
from django.forms import TextInput,Textarea,Select,RadioSelect

class ProfileForm(forms.ModelForm):
     class Meta:
        model=Profile
        exclude = ['user','role','zayavl']
        widgets = {
            'familiya':TextInput(attrs={'class':'form-control'}),
            'imya':TextInput(attrs={'class':'form-control'}),
            'otchestvo':TextInput(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'seriya':TextInput(attrs={'class':'form-control'}),
            'nomer':TextInput(attrs={'class':'form-control'}),
            'special':Select(attrs={'class':'custom-select d-block w-100'}),
            'facult':Select(attrs={'class':'custom-select d-block w-100'}),
            'russ':TextInput(attrs={'class':'form-control'}),
            'mat':TextInput(attrs={'class':'form-control'}),
            'obsh':TextInput(attrs={'class':'form-control'}),
            'pol':RadioSelect(),

            'biol':TextInput(attrs={'class':'form-control'}),
            'dostizh':Select(attrs={'class':'custom-select d-block w-100'}),
            'organ':Select(attrs={'class':'custom-select d-block w-100'}),
            'osobpravo':Select(attrs={'class':'custom-select d-block w-100'}),

        }
