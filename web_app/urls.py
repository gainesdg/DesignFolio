from django.urls import path
from web_app import views

app_name = 'design-grid'
urlpatterns = [
    path('', views.index, name='index'),
    #path('profession/<slug:profession_name_slug>/', views.show_category, name='show_category'),
    #path('user/<slug:user_name_slug>/add_page/', views.add_page, name = 'add_page'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]