from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'user_image', 'user_age', 'user_description')
