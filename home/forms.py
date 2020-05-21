from django import forms
from home.models import Profile,OsobDocument,DostizhDocument
from django.forms import TextInput,Textarea,Select,RadioSelect,FileInput


class ProfileForm(forms.ModelForm):
    DOST = (('a','a'),
               ('b','b'),
               ('c','c'),
               ('d','d'),)
    dost = forms.MultipleChoiceField(required=False,choices=DOST, widget=forms.CheckboxSelectMultiple())
    OSOB = (('a','a'),
               ('b','b'),
               ('c','c'),
               ('d','d'),)
    osob = forms.MultipleChoiceField(required=False,choices=OSOB, widget=forms.CheckboxSelectMultiple())
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
    def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']
        return super(ProfileForm, self).save(commit=commit)
class OsobDocumentForm(forms.ModelForm):
    class Meta:
        model=OsobDocument
        fields = ['name','type','doc',]
        widgets = {'name':TextInput(attrs={'class':'form-control formaeb','placeholder':'название документа'}),
                   'type':TextInput(attrs={'class':'form-control formaeb','disabled':'disabled'}),
                   'doc':FileInput(attrs={'class':'formaeb'}),
        }

class DostizhDocumentForm(forms.ModelForm):
    doc = forms.FileField(label=('Company Logo'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model=DostizhDocument
        fields = ['name','type','doc']
        widgets = {'name':TextInput(attrs={'class':'form-control formaeb','placeholder':'название документа'}),
                   'type':TextInput(attrs={'class':'form-control formaeb','disabled':'disabled'}),
                   'doc':FileInput(attrs={'class':'formaeb','disabled':'disabled'}),
        }
class ZayavlForm(forms.ModelForm):
    zayavl = forms.FileField(label=(''),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model=Profile
        fields = ['zayavl',]
        widgets = {
                   'zayavl':FileInput(attrs={'class':'formaeb','disabled':'disabled'}),
        }
class AdminForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['familiya','dopusk','balli']
        widgets = {
        }
