import bcrypt
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User, UserManager
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_reg(request):
    return render(request, 'reg_form.html')

def reg_user(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('show_reg')
    else:
        request.session['id'] = request.POST['id']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            id = request.session['id'],
            name = request.POST['name'],
            email = request.POST['email'],
            password = pw_hash,
        )
        return redirect('dashboard')

def show_login(request):
    return render(request, 'login_form.html')

def login_user(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password = password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    return redirect('')