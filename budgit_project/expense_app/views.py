from django.shortcuts import HttpResponse, render

from . import models

# Create your views here.
# def index(request):
#     return HttpResponse('Login/Register Page')

def index(request):
    context = {
        "user": 'Sarah',
        'data': ['Rent', '$1200', 'Housing', 'Yes']
    }
    return render(request, "dashboard.html", context)

def add_expense(request):
    context = {
        "page_name": 'Add an Expense',
        'model': models.Expense,
    }
    return render(request, "expense_form.html", context)
