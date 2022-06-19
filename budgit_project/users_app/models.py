from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email address!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email address!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        return errors

class User(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid1,
    #     editable=False
    # )
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    password = models.CharField(max_length=128, blank=False)
    objects = UserManager()
