from django import forms
from . import models

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = models.Expense
        fields = ['name', 'amount', 'category', 'recurring']
        labels = {
            'name': 'Expense Name',
            'amount': 'Amount',
            'category': 'Category',
            'recurring': 'Recurring?',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
            }),
            'amount': forms.IntegerField(attrs={
                'type': 'integer',
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'type': 'text',
                'class': 'form-control',
            }),
            'recurring': forms.CheckboxInput(attrs={
                'type': 'boolean',
                'class': 'form-control',
            })
        }