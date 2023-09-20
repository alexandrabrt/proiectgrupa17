from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(['Emailul deja exista! Te rugam sa adaugi alt email'])
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['Usernameul exista! Te rugam sa alegi altul'])
        return field_data
