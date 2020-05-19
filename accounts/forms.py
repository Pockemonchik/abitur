from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
))

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', )
        widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'password':TextInput(attrs={'class':'form-control'}),
            }
