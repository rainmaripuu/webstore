from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import StoreUser


class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(render_value=True))




    # class Meta:
    #     model = StoreUser
    #     fields = ('username', 'email', 'password1', 'password2', )