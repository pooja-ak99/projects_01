from django.shortcuts import render, redirect
from Shop.models import category, product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def allcategories(request):
    c = category.objects.all()
    return render(request, 'allcategories.html', {"allcat":c})

def allproducts(request,p):
    c = category.objects.get(name=p)
    p = product.objects.filter(category=c)
    return render(request, 'allproducts.html', {"allcat1":c, "allpro":p})

def productdetails(request,d):
    p = product.objects.get(id=d)
    return render(request, 'productdetails.html', {"allpro1":p})

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        if (p==cp):
            if (e==""):
                return HttpResponse("Email needed")
            else:
                u = User.objects.create_user(username=u,password=p,email=e)
                u.save()
                return redirect("Shop:home")
        else:
            return HttpResponse("Password not matching")
    return render(request, 'register.html')

def user_login(request):
    if(request.method=="POST"):
        un = request.POST['u']
        pw = request.POST['p']
        user = authenticate(username=un,password=pw)
        if user:
            login(request,user)
            return redirect("Shop:home")
        else:
            messages.error(request,"**INVALID CREDENTIALS**")
    return render(request, "login.html")

@login_required()
def user_logout(request):
    logout(request)
    return redirect("Shop:home")

