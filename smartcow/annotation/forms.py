from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Photo, Annotate


class SignUpForm(UserCreationForm):
    project_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'project_name')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)


class AnnotateForm(forms.ModelForm):
    class Meta:
        model = Annotate
        fields = "__all__"
