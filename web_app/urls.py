from django.urls import path, include
from web_app import views

app_name = 'design-grid'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('profession/<slug:profession_name_slug>/', views.profession, name='profession'),
    path('user/<slug:user_name_slug>/', views.profile, name = 'profile'),
    path('post/<posts_pid>/', views.post, name = 'post'),

    path('search/<argument>/', views.search, name='search'),
    path('profession_filter/', views.profession_filter, name='profession_filter'),

    path('create-post/', views.add_post, name='add_post'),
    path('add-section/', views.add_section, name='add_section'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add-link/', views.add_link, name='add_link'),
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]
