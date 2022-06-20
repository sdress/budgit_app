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
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('show_reg')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            password = pw_hash,
        )
        request.session['user_id'] = user.id
        return redirect('dashboard')

def show_login(request):
    return render(request, 'login_form.html')

def login_user(request):
    user_email = request.POST['email']
    user_password = request.POST['password']
    pw_hash = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
    user = authenticate(email=user_email, password = pw_hash)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.add_message(request, messages.INFO, 'Unable to login, please try again')
        return redirect('show_login')

def logout_user(request):
    logout(request)
    request.session.clear()
    return redirect('index')