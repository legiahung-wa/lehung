from django.shortcuts import render, redirect
from .models import Product,Staff
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(req):
    data= Product.objects.all()
    return render(req, 'home.html',context={'data':data}) 

def signin(req):
    return render(req, 'signin.html')
def signup(req):
    return render(req, 'signup.html')

def getStaff(req):
    staff= Staff.objects.all()
    return render(req,'staff.html',context={'data':staff})
def login_user(req):
    if req.method =="POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req,username = username, password = password)
        if user is not None:
            return redirect("home")
        else:
            return redirect('login')
    else:
        return render(req,'login.html')
    
def logout_user(req):
    logout(req)
    return redirect("home")