from sre_parse import CATEGORIES
from django.db import models

# Create your models here.
class User(models.Model):
    pass

class Expense(models.Model):
    # Expense category choices
    # from docs: https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
    CATEGORIES = (
        ('H', 'Housing'),
        ('T', 'Transportation'),
        ('F', 'Food'),
        ('I', 'Insurance'),
        ('U', 'Utilities'),
        ('E', 'Entertainment'),
        ('M', 'Medical/Healthcare'),
        ('S', 'Supplies/Toiletries'),
        ('P', 'Personal'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=50, blank=False, editable=True, help_text='Please include a name')
    amount = models.IntegerField(blank=False, editable=True, help_text='Value must be at least $1')
    category = models.CharField(max_length = 50,choices=CATEGORIES, blank=True, editable=True)
    # default form widget is checkboxinput
    # source: https://docs.djangoproject.com/en/4.0/ref/models/fields/#booleanfield
    recurring = models.BooleanField(default='False', null=False, editable=True)

    def get_choices(self):
        return list(Expense.CATEGORIES)