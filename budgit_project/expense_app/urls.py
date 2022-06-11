from urllib import request
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.ExpenseListView.as_view(), name='dashboard'),
    # path('expenses/add', views.add_expense, name='expense_form')
]
