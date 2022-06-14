from urllib import request
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('expenses/add', views.add_expense, name='expense_form'),
    path('expenses/save', views.save_expense, name='save_expense'),
]
