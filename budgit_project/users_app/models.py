from django.db import models
import re
from django.contrib.auth.hashers import check_password

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['username']) < 2:
            errors['username'] = 'Username must be at least 2 characters'
        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email address'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if postData['password'] != postData['pass_confirm']:
            errors['password'] = 'Passwords must match'
        return errors

    def login_validator(self, postData):
        errors = {}
        try:
            User.objects.get(email=postData['email'])
        except User.DoesNotExist:
            errors['email'] = 'Email does not exist'
            return errors
        user = User.objects.get(email=postData['email'])
        # print(user.password)
        # if check_password(postData['password'], user.password):
        #     print(check_password(postData['password'], user.password))
        #     errors['password'] = 'Incorrect password'
        # user = User.objects.filter(email=postData['email'])[0]
        return errors

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    password = models.CharField(max_length=128, blank=False)
    objects = UserManager()

    def __str__(self):
        return f'user: {self.email}'