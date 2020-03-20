from django import forms
from web_app.models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    profession = forms.ModelChoiceField(queryset=Profession.objects.all())
    
    class Meta:
        model = UserProfile
        fields = ('profession',)#('picture','location','bio','available', 'profession')


class CreatePostForm(forms.ModelForm):
    
    def __init__(self,user=None,*args,**kwargs):
        super (CreatePostForm,self ).__init__(*args,**kwargs) # populates the post
        if user!=None:
            self.fields['section'].queryset = Section.objects.filter(user=user)
            self.fields['profession'] = UserProfile.objects.filter(user=user)[0].profession
            self.fields['section'].help_text = "Section"

    title = forms.CharField(max_length=128, help_text="Title")
    description = forms.CharField(max_length=512, help_text="Description")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Posts
        fields = ('picture', 'section', 'title', 'description')



class CreateSectionForm(forms.ModelForm):
    def __init__(self,user=None,*args,**kwargs):
        super (CreateSectionForm,self ).__init__(*args,**kwargs) # populates the post
        if user!=None:
            self.fields['user'].queryset = user

    name = forms.CharField(max_length=128, help_text="Name")

    class Meta:
        model = Section
        fields = ('name',)