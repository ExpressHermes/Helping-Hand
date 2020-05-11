from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create_event/', views.create_event, name='create_event'),
]
