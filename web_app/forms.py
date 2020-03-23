from django import forms
from web_app.models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

#Enter user details
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

#Enter profile profession for initial sign up
class UserProfileForm(forms.ModelForm):

    profession = forms.ModelChoiceField(queryset=Profession.objects.all())
    
    class Meta:
        model = UserProfile
        fields = ('profession',)
        exclude = ('picture','location','bio','available')

#Edit the user profile
class EditProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        user = kwargs.get('instance')
        if user:
            #Set the initial values of each field to what the users profile
            #is currently looking like
            self.fields['picture'].initial = user.picture
            self.fields['location'].initial = user.location
            self.fields['bio'].initial = user.bio
            self.fields['available'].initial = user.available

    location = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user','profession','slug')
        fields = ('location','bio','picture','available')

#Create a post
class CreatePostForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super (CreatePostForm,self ).__init__(*args,**kwargs)

        if user:
            self.fields['section'].queryset = Section.objects.filter(user=user)
            self.fields['section'].help_text = "Section"

    title = forms.CharField(max_length=128, help_text="Title")
    description = forms.CharField(max_length=512, help_text="Description")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Posts
        fields = ('picture', 'section', 'title', 'description')
        exclude = ('profession',)

#Checkbox menu to specify what tags to include when creating a post
class IncludeTagForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        tag = kwargs.get('instance')
        super (IncludeTagForm,self ).__init__(*args,**kwargs)

        if tag:
            self.fields['tag'] = tag

    checkbox = forms.BooleanField()

    class Meta:
        model = PostTags
        fields = ('tag',)

#Create a section for the user
class CreateSectionForm(forms.ModelForm):

    name = forms.CharField(max_length=64, help_text="Name")

    class Meta:
        model = Section
        fields = ('name',)
        exclude = ('user',)


#Add a link to the user profile
class UserLinksForm(forms.ModelForm):

    class Meta:
        model = UserLinks
        fields = ('site_name', 'link')

"""
class professionTagFilterForm(forms.ModelForm):
    name = 

    class Meta:
        model = Tags
        fields = ('name',)
"""