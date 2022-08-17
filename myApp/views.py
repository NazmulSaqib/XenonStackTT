from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            context = {'flag':True, 'msg':'SignUp Succesfully'}
            return render(request, 'myApp/login.html', context)
    context = {'form':form}
    return render(request, 'myApp/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:  
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                contex = {'flag':True, 'msg':'Logged in succesfully'}
                return render(request, 'myApp/home.html', contex)
        context = {'flag':False}
        return render(request, 'myApp/login.html', context)

def logoutPage(request):
    logout(request)
    context = {'flag':True, 'msg':'Logout Successfully'}
    return render(request, 'myApp/home.html', context)

def contact(request):
    form = QureyForm()
    if request.method == 'POST':
        form = QureyForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'flag':True, 'msg':'From submitted successfully'}
            return render(request, 'myApp/home.html', context)
    context = {'form':form}
    return render(request, 'myApp/contact.html', context)
     
