from django.urls import path
from web_app import views

app_name = 'design-grid'
urlpatterns = [
path('', views.index, name='index'),
]