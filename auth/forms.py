from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from user.models import InstaUser


class UserLoginForm(AuthenticationForm):
    username = UsernameField(max_length=254,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("Email")}))
    password = forms.CharField(label=_("Password"), strip=False,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': _("Password")}))


class UserRegistrationForm(forms.ModelForm):
    retype_password = forms.CharField(label=_('Retype password'), max_length=128,
                                      widget=forms.PasswordInput(
                                          attrs={'class': 'form-control', 'placeholder': _('Retype password')}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        retype_password = cleaned_data.get('retype_password')

        if password and retype_password and password != retype_password:
            self.add_error('retype_password', forms.ValidationError(_('Password does not match')))

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        return user

    class Meta:
        model = InstaUser
        fields = ('email', 'first_name', 'last_name', 'password',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Enter email')}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter first name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter last name')}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Type password')}),
        }


class PasswordUpdateForm(PasswordChangeForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
