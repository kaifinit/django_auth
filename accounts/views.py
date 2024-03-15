from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def accounts_view(request):
    # if request.user.is_authenticated:
        # return redirect('main')
    return redirect('main')


def register_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username is None or username == '':
            messages.error(request, 'username is required!')
            return render(request, 'accounts/register.html')
        if password is None or password == '':
            messages.error(request, 'password is required!')
            return render(request, 'accounts/register.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'User created successfuly')
        return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # check username validation
        if username is None or username == '':
            messages.error(request, 'username is required!')
            return render(request, 'accounts/register.html')
        # check password validation
        if password is None or password == '':
            messages.error(request, 'password is required!')
            return render(request, 'accounts/register.html')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, 'logged in successfuly')
        next_url = request.GET.get('next', '/')
        return redirect(next_url)
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    next_url = request.GET.get('next', '/')
    return redirect(next_url)