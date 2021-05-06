from datetime import datetime
from apps.account.models import RegisterUser
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_page

def register_user(request):
    if request.method=="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = True
            user.save()
            reg = RegisterUser(user=user)
            reg.save()
            return render(request,"account/signup.html",{"status":"Mr/Miss. {} your Account created Successfully".format(first_name)})
        except IntegrityError as e: 
            return render(request,"account/signup.html",{"status":"Mr/Miss. {} already ".format(username)})
    return render(request,"account/signup.html")
# import pdb; pdb.set_trace()---for debug purpose
@login_required
def user_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/signin")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    messages.success(request,"Successfully Logged Out")
    return res


@cache_page(30)
def user_login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            if user.is_authenticated:
                if user.is_superuser:
                    return HttpResponseRedirect("index")
                else:
                    messages.success(request," Successfully Logged in ")
                    res = HttpResponseRedirect("index")
                    if "rememberme" in request.POST:
                        res.set_cookie("user_id",user.id)
                        res.set_cookie("date_login",datetime.now())
                    return res
            else:
                return HttpResponseRedirect("index")
        else:
            messages.success(request,"Incorrect username or Password")
            return render(request,"account/login.html")

    return render(request,"account/login.html")

def check_user(request):
    if request.method=="GET":
        username = request.GET["usern"]
        check = User.objects.filter(username=username)
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

def change_password(request):
    context={}
    ch = RegisterUser.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = RegisterUser.objects.get(user__id=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            messages.success(request," Password Changed Successfully!!! ")
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            messages.success(request," Incorrect Current Password!!! ")
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"account/change_password.html",context)


