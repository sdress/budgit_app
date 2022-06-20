from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('new', views.add_expense, name='expense_form'),
    path('save', views.create_expense, name='create_expense'),
    path('edit/<int:id>', views.edit_expense, name='edit_expense'),
]
