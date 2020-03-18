from django import forms
from rango.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','location','bio','available','link1','link2','link3')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('section', 'picture', 'title', 'description', 'tags')