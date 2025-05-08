from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'auth/home.html')

def logic(request):
    return render(request, 'logic.html')

def work(request):
    return render(request, 'work.html')

def about(request):
    return render(request, 'about.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
        messages.error(request, "Login yoki parol noto'g'ri")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Avtomatik login qilish
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')