from django.shortcuts import HttpResponse, render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

from . import models

# Create your views here.
# def index(request):
#     return HttpResponse('Login/Register Page')

# def index(request):
#     context = {
#         "user": 'Sarah',
#         'data': 
#     }
#     return render(request, "dashboard.html", context)

# def add_expense(request):
#     context = {
#         "page_name": 'Add an Expense',
#         'model': models.Expense,
#     }
#     return render(request, "expense_form.html", context)

class ExpenseListView(generic.ListView):
    model = models.Expense
    form_class = forms.ExpenseForm