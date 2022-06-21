import bcrypt
from django.shortcuts import redirect, render
from django.contrib import messages, sessions
from .models import User, UserManager
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_reg(request):
    return render(request, 'reg_form.html')

def reg_user(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('show_reg')
    else:
        user = User.objects.create(
            username = request.POST['username'],
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        user.is_active = True
        # user.set_password(request.POST['password'])
        print(user)
        request.session['user_id'] = user.id
        return redirect('dashboard')

def show_login(request):
    return render(request, 'login_form.html')

def login_user(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('show_login')
    else:
        user_check = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user_check)
        user = User.objects.get(email=request.POST['email'])
        # print(User.objects.get(id=1))
        request.session['user_id'] = user.id
        return redirect('dashboard')

def logout_user(request):
    logout(request)
    request.session.clear()
    return redirect('index')