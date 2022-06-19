from multiprocessing.sharedctypes import Value
from queue import Empty
from sre_constants import LITERAL
from sre_parse import CATEGORIES
from uuid import uuid1
from django.db import models
from django.db.models import Sum
import re
import bcrypt
from django.forms import NumberInput

# Create your models here.

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email address!'
        
        return errors

class User(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid1,
    #     editable=False
    # )
    # name = models.CharField(max_length=255, blank=False)
    # email = models.EmailField(max_length=255, blank=False)
    # password = models.CharField(max_length=128, blank=False)
    pass

class ExpenseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        if len(postData['amount']) < 1:
            errors['amount'] = 'Please input an amount'
        if Value(postData['amount']) < 1:
            errors['amount'] = 'Amount must be greater than $1'
        if postData['recurring'] == Empty:
            errors['recurring'] = 'Please make a selection'
        return errors

class Expense(models.Model):
    # Expense category choices
    # from docs: https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
    CATEGORIES = [
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
    ]
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid1,
    #     editable=False
    # )
    name = models.CharField(max_length=50, blank=False, editable=True)
    amount = models.IntegerField(blank=False, editable=True)
    category = models.CharField(max_length = 50,choices=CATEGORIES, blank=True, editable=True)
    # default form widget is checkboxinput
    # source: https://docs.djangoproject.com/en/4.0/ref/models/fields/#booleanfield
    recurring = models.BooleanField(default='False', null=False, editable=True)
    # user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    objects = ExpenseManager()

    def get_choices():
        return list(Expense.CATEGORIES)
        # return Expense.get_category_display()
    
    def get_total():
        total = Expense.objects.aggregate(Sum('amount'))['amount__sum']
        return total