from django import forms
from django.utils.translation import ugettext_lazy as _


class UserUpdateForm(forms.Form):
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label=_('First name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_('Last name'), widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.CharField(label=_('Image'), widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if email:
            self.user.email = email
        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.save()
        return self.user
