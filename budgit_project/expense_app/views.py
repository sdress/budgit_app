from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy

from .models import Expense
from users_app.models import User
from . import forms

# class ExpenseListView(generic.ListView):
#     model = models.Expense
#     form_class = forms.ExpenseForm

def dashboard(request):
    data = Expense.objects.all()
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user.name,
        'data': data,
        'total': Expense.get_total()
    }
    # print(context['data'])
    return render(request, 'dashboard.html', context)

def add_expense(request):
    context = {
        "page_name": 'Add an Expense',
        'categories': Expense.get_choices(),
    }
    return render(request, "expense_form.html", context)

def save_expense(request):
    errors = Expense.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('expense_form')
    else:
        Expense.objects.create(name=request.POST['name'], amount=int(request.POST['amount']), category=request.POST['category'], recurring=request.POST['recurring'])
        return redirect('dashboard')

def edit_expense(request, id):
    context = {
        'page_name': 'Edit Expense',
        'exp': Expense.objects.get(id=id),
        'categories': Expense.get_choices(),
    }
    return render(request, 'expense_edit.html', context)