from django import forms
from web_app.models import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    profession = forms.ModelChoiceField(queryset=Profession.objects.all())
    
    class Meta:
        model = UserProfile
        fields = ('profession',)#('picture','location','bio','available', 'profession')

class EditProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        user = kwargs.get('instance')
        if user:
            kwargs['instance'] = user

        self.user_form = UserProfileForm(*args, **kwargs)

        self.fields.update(self.user_form.fields)
        self.initial.update(self.user_form.initial)

    def save(self, *args, **kwargs):
        self.user_form.save(*args, **kwargs)
        return super(EditProfileForm, self).save(*args, **kwargs)
    
    location = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user','profession','slug')
        fields = ('location','bio','picture','available')


class CreatePostForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super (CreatePostForm,self ).__init__(*args,**kwargs) # populates the post
        user = kwargs.get('instance')

        try:
            print(user)
            self.fields['section'].queryset = Section.objects.filter(user=user)
            self.fields['section'].help_text = "Section"
            self.fields['profession'] = UserProfile.objects.get(user=user).profession
        except Exception as e:
            print('e',e)


    title = forms.CharField(max_length=128, help_text="Title")
    description = forms.CharField(max_length=512, help_text="Description")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    

    class Meta:
        model = Posts
        fields = ('picture', 'section', 'title', 'description')

"""
class PostTagsForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super (CreatePostForm,self ).__init__(*args,**kwargs) # populates the post
        post = kwargs.get('instance')
        self.field['post'] = post

    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=post.profession)

    class Meta:
        model = PostTags
        fields = ('tag',)
"""


class CreateSectionForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (CreateSectionForm,self ).__init__(*args,**kwargs) # populates the post
        user = kwargs.get('instance')

        self.fields['user'] = user

    name = forms.CharField(max_length=128, help_text="Name")

    class Meta:
        model = Section
        fields = ('name',)


"""
class UserLinksForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super (CreatePostForm,self ).__init__(*args,**kwargs) # populates the post
        user = kwargs.get('instance')
        self.field['user'] = user

    class Meta:
        model = UserLinks
        fields = ('site_name', 'link')

"""