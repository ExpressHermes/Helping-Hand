from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('activate/<uidb64>/<token>/', views.user_verify, name="activate"),  
    path('ForgotPassword/', views.forgot_password, name="forgot_password"), 
    # path('ResetPassword/<uidb64>/<token>/', views.reset_password, name="reset_password"),  
    # path('ResetPasswordDone/', views.reset_password_done, name="reset_password_done"),  
 
]
