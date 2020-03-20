from django.urls import path
from web_app import views

app_name = 'design-grid'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('profession/<slug:profession_name_slug>/', views.profession, name='profession'),
    path('user/<slug:user_name_slug>/', views.profile, name = 'profile'),
    path('post/<slug:posts_pid_slug>/', views.post, name = 'post'),

    path('create-post/', views.add_post, name='add_post'),
    path('add-section/', views.add_section, name='add_section'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
