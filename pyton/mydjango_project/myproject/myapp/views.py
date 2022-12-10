from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.contrib.auth.models import User ,auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hey .welcome </h1>")
    # name= "aycode"
    # feature1=Feature()
    # feature1.id=0
    # feature1.name="canvass"
    # feature1.is_true= True
    # feature1.details="our service is very quick"

    # feature2=Feature()
    # feature2.id=1
    # feature2.name="endorse"
    # feature2.is_true= False
    # feature2.details="our service is very quick"
    
    # feature3=Feature()
    # feature3.id=2
    # feature3.name="support"
    # feature3.is_true= True
    # feature3.details="our service is very quick"
     
     
    # context ={
    #     "name":"Aycode",
    #     "age" : 23,
    #     "nationality":"British"
    # }
    
    features=Feature.objects.all()

    return render(request,"index.html" ,  {"features":features})


def counter(request):
     posts=[1,2,3,4,5,"tim","tom","john"]
     return render(request,"counter.html",{"posts":posts})


def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("register") 
            else:
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"password not same")
            return redirect("register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password =request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Credential Invalid")
            return redirect("login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def post (request,pk):
   return render(request,"post.html",{"pk":pk})