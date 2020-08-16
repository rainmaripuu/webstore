from django import forms
from store.models import StoreUser


class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError(
                "password and password confirmation does not match"
            )

        username = cleaned_data.get('username')
        existing_user = StoreUser.objects.filter(username=username)

        if existing_user.count() != 0:
            raise forms.ValidationError(
                "This username is already taken. Choose another one"
            )