from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AvatarFileUploadInput(forms.ClearableFileInput):
    template_name = "widgets/upimagem.html"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('imagem', 'discord_id')
        widgets = {"imagem": AvatarFileUploadInput }


