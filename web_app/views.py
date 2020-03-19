from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from web_app.models import *

#Display the home page
def index(request):
    professions_list = Profession.objects.all()
    context_dict={}
    context_dict['professions']= professions_list
    return render(request, 'web_app/index.html', context_dict)

#Display the professions page
def profession(request, profession_name_slug):
    context_dict = {}

    try:
        #Get the profession that matches the profession in the URL
        profession = Profession.objects.get(slug=profession_name_slug)
        tags = Tags.objects.filter(profession=profession)
        
        context_dict['tags'] = tags
        context_dict['profession'] = profession

        return render(request, 'web_app/profession.html', context_dict)

    except Profession.DoesNotExist:
        #If the url does not have an existing profession show an error page
        context_dict['item'] = ''.join(('Profession, ', profession_name_slug, ','))
        return render(request, 'web_app/missing_content.html', context_dict)

#Display the Profile Page
def profile(request, user_name_slug):
    context_dict = {}
    try:
        #Get the user that matches the user slug in the URL
        user = UserProfile.objects.get(slug=user_name_slug)

        #add user info to context dictionary
        context_dict['username'] = user.user.username
        context_dict['location'] = user.location
        context_dict['bio'] = user.bio
        #if user is available, add the "Available" message and their email
        if user.available:
            context_dict['available'] = "Available"
            context_dict['email'] = user.user.email
        else:
            context_dict['available'] = "Not Available"
            context_dict['email'] = ''
        
        #add the users external links
        links = UserLinks.objects.filter(user=user.user)
        context_dict['links'] = {} 
        #dictionary of key, site name, and value, URL
        for link in links:
            context_dict['links'][link.site_name] = link.link

        #Add the sections and posts within the sections owned by the user
        sections = Section.objects.filter(user=user.user)
        context_dict['sections'] = {}

        for section in sections:
            posts = Posts.objects.filter(section = section)
            context_dict['sections'][section.name]=posts
    
        return render(request, 'web_app/profile.html', context_dict)

    #If the URL contains a user name that does not exist show error page
    except UserProfile.DoesNotExist:
        context_dict['item'] = ''.join(('User, ', user_name_slug, ','))
        return render(request, 'web_app/missing_content.html', context_dict)

    
def post(request, posts_pid_slug):
    context_dict={}
    try:
        post = Posts.objects.get(slug=posts_pid_slug)
        context_dict['post'] = post

        tags = PostTags.objects.filter(post=post)
        context_dict['tags']=tags 

        return render(request, 'web_app/post.html', context_dict)

    except Posts.DoesNotExist:
        context_dict['item'] = ''.join(('Post with ID:, ', posts_pid_slug, ','))
        return render(request, 'web_app/missing_content.html', context_dict)


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'web_app/register.html', context={'user_form': user_form, 'profile_form': profile_form,\
                                                           'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('web_app:index'))
            else:
                return HttpResponse('Your DesignGrid account is disabled.')
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'web_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('web_app:index'))
