from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('map/', views.map, name='map'),
]
