from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', include('register.urls')),
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]
