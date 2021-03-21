from django import forms


class UserNameForm(forms.Form):
    username = forms.CharField(label='Github username: ', max_length=50)
