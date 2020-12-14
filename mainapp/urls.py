from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create_event/', views.create_event, name='create_event'),
    path('<str:username>/dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
