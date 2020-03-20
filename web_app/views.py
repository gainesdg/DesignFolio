from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from web_app.models import *
from web_app.forms import *

#Display the home page
def index(request):
    #List every profession in database
    professions_list = Profession.objects.all()
    context_dict={}
    context_dict['professions']= professions_list
    return render(request, 'web_app/index.html', context_dict)

#Display the professions page
def profession(request, profession_name_slug):
    context_dict = {}

    try:
        #Get the profession that matches the profession in the URL
        #Get the tags and posts related to this profession
        profession = Profession.objects.get(slug=profession_name_slug)
        tags = Tags.objects.filter(profession=profession)
        posts = Posts.objects.filter(profession=profession)
        
        #store relevant tags and professions
        context_dict['tags'] = tags
        context_dict['profession'] = profession
        context_dict['posts'] = posts

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
        context_dict['profile'] = user

        #if user is available, add the "Available" message and their email
        if user.available:
            context_dict['available'] = "Available"
            context_dict['email'] = user.user.email
        else:
            context_dict['available'] = "Not Available"
            context_dict['email'] = ''
        
        #add the users external links e.g instagram or facebook
        links = UserLinks.objects.filter(user=user.user)
        context_dict['links'] = {} 
        #dictionary of key: site name, and value: URL
        for link in links:
            context_dict['links'][link.site_name] = link.link

        #Add the sections and posts within the sections owned by the user
        sections = Section.objects.filter(user=user.user)
        context_dict['sections'] = {}

        for section in sections:
            posts = Posts.objects.filter(section = section)
            context_dict['sections'][section.name]=posts

        #Boolean to check if the user is viewing their own page
        context_dict['owner'] = (user.user == request.user)

        return render(request, 'web_app/profile.html', context_dict)

    #If the URL contains a user name that does not exist show error page
    except UserProfile.DoesNotExist:
        context_dict['item'] = ''.join(('User, ', user_name_slug, ','))
        return render(request, 'web_app/missing_content.html', context_dict)

    
def post(request, posts_pid_slug):
    context_dict={}
    try:
        #Find the post with the matching ID in the URL
        post = Posts.objects.get(slug=posts_pid_slug)
        context_dict['post'] = post

        #Get the tags of this post
        tags = PostTags.objects.filter(post=post)
        context_dict['tags']=tags 

        #Find the creater of the post. Section has attribute user, post has attribute section
        user = post.section.user
        profile = UserProfile.objects.get(user=user)
        context_dict['profile']=profile

        return render(request, 'web_app/post.html', context_dict)

    #If the URL containing the post ID does not exist, show error page
    except Posts.DoesNotExist:
        context_dict['item'] = ''.join(('Post with ID: ', posts_pid_slug, ','))
        return render(request, 'web_app/missing_content.html', context_dict)





def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


@login_required
def add_post(request):        
    form = CreatePostForm()
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = CreatePostForm(user, request.POST)
    
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new post to the database.
            form.save(commit=True)
            
            post_pid_slug = Posts.objects.get(section=Section.objects.get(user=user)).slug
            return redirect(reverse('design-grid:post', kwargs={'posts_pid_slug': posts_pid_slug } ))
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
            
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'web_app/add_post.html', {'form': form})

@login_required
def add_section(request):
    form = CreateSectionForm()
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = CreatePostForm(user, request.POST)
    
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new post to the database.
            form.save(commit=True)
            
            user_name_slug = UserProfile.objects.get(user=user).slug
            return redirect(reverse('design-grid:profile', kwargs={'user_name_slug': user_name_slug } ))
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
            
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'web_app/add_post.html', {'form': form})


@login_required
def edit_profile(request):
    return HttpResponse(request, 'EDIT PROFILE')


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #include profession and link user to user profile
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'web_app/register.html', context={'user_form': user_form, 'profile_form': profile_form,
                                                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)

                user_name_slug = UserProfile.objects.get(user=user).slug
                return redirect(reverse('design-grid:profile', kwargs={'user_name_slug': user_name_slug } ))
            else:
                # An inactive account was used - no logging in
                return HttpResponse('Your DesignGrid account is disabled.')
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render(request, 'web_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('design-grid:index'))
