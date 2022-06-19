from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.show_login, name='show_login'),
    path('login-user', views.login_user, name='login_user'),
    path('register', views.show_reg, name='show_reg'),
    path('create-user', views.reg_user, name='create_user')
]