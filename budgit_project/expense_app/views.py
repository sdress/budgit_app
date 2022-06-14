from queue import Empty
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Expense, User
from . import forms

# class ExpenseListView(generic.ListView):
#     model = models.Expense
#     form_class = forms.ExpenseForm

def dashboard(request):
    data = Expense.objects.all()
    context = {
        'user': 'Sarah',
        'data': data,
        'total': Expense.get_total()
    }
    # print(context['data'])
    return render(request, 'dashboard.html', context)

def add_expense(request):
    context = {
        "page_name": 'Add an Expense',
        'model': Expense,
    }
    return render(request, "expense_form.html", context)

def save_expense(request):
    if request.POST['recurring'] == 'on':
        response = 'yes'
    else:
        response = 'no'
    context = {
        'name': request.POST['name'],
        'amount': request.POST['amount'],
        'category': request.POST['category'],
        'recurring': response,
    }
    # new_exp = models.Expense(name=request.POST['name'], amount=request.POST['amount'], category=request.POST['category'], recurring=request.POST['recurring'] == 'on')
    new_exp = Expense(context)
    new_exp.save()
    return redirect('dashboard')