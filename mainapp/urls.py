from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create_event/', views.create_event, name='create_event'),
    path('food', views.food, name='food'),
    path('medical', views.medical, name='medical'),
    path('others', views.others, name='others'),
    path('clothes', views.clothes, name='clothes'),

]
