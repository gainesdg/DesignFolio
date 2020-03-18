from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from web_app.models import *
# Create your views here.

def index(request):
    professions_list = Profession.objects.all()
    context_dict={}
    context_dict['professions']= professions_list
    return render(request, 'web_app/index.html', context_dict)

def profession(request, profession_name_slug):
    context_dict = {}

    try:

        profession = Profession.objects.get(slug=profession_name_slug)
        tags = Tags.objects.filter(profession=profession)
        
        context_dict['tags'] = tags
        context_dict['profession'] = profession
    except Profession.DoesNotExist:
        context_dict['profession'] = "Profession not found."
        context_dict['tags'] = None
    return render(request, 'web_app/profession.html', context_dict)


def profile(request, user_name_slug):
    context_dict = {}
    try:
        user = UserProfile.objects.get(slug=user_name_slug)

        context_dict['username'] = user.user.username
        context_dict['location'] = user.location
        context_dict['bio'] = user.bio
        if user.available:
            avail = ''.join(("Available\n",user.user.email))
            context_dict['available'] = avail
        else:
            context_dict['available'] = "Not Available"
        """
        context_dict['link1'] = user.link1
        context_dict['link2'] = user.link2
        context_dict['link3'] = user.link3
        """
    except Profession.DoesNotExist:
        context_dict['username'] = "User not found."
        context_dict['location'] = None
        context_dict['bio'] = None
        context_dict['available'] = None

    return render(request, 'web_app/profile.html', context_dict)


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
