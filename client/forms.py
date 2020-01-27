from django import forms

from client.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('instagram_username', 'instagram_password',)
        widgets = {
            'instagram_username': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
