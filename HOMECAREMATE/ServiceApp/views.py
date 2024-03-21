from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from ServiceApp.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ServiceApp.models import Category, Career, Booking
from ServiceApp.forms import Categoryform


def home(request):
    return render(request, "home.html")

@login_required()
def categorypage(request,c1):
    c = Category.objects.get(category_name=c1)
    p = c.pointlist()
    return render(request, "categorypage.html", {'cat':c,'poi':p})

@login_required()
def allcategory(request):
    return render(request, 'allcategory.html')

@login_required()
def booking(request):
    if request.method == "POST":
        n = request.POST['n']
        e = request.POST['e']
        p = request.POST['p']
        c = request.POST.get('c')
        s = Category.objects.get(category_name=c)
        d = request.POST['d']
        r = request.POST['r']
        b = Booking.objects.create(name=n, email=e, phone=p, service_date=d, service=s, special_request=r)
        b.save()
        return home(request)
    return render(request, 'booking.html')

def career(request):
    return render(request, 'career.html')

def careerapplication(request):
    if request.method == "POST":
        n = request.POST['n']
        b = request.POST['b']
        p = request.POST['p']
        e = request.POST['e']
        a = request.POST['a']
        q = request.POST['q']
        s = request.POST['s']
        l = request.POST['l']
        g = request.POST['g']
        r = request.FILES['r']
        i = request.FILES['i']
        f = request.FILES['f']
        z = Career.objects.create(fullname=n, dob=b, phone=p, email=e, address=a,qualification=q, location=l, gender=g,
                                  skills=s, resume=r, id_proof=i, profile_photo=f)
        z.save()
        return redirect('careerapplications')
    return render(request, 'careerapplication.html')

def careerapplications(request):
    return render(request, 'careerapplications.html')

@login_required()
def applicationslist(request):
    a = Career.objects.all()
    return render(request, 'applicationslist.html', {'a1':a})

@login_required()
def delete(request,p):
    p = Career.objects.get(id=p)
    p.delete()
    return render(request, 'applicationslist.html')

@login_required()
def bookinglist(request):
    b = Booking.objects.all()
    return render(request, 'bookinglist.html', {'book':b})

@login_required()
def remove(request,p):
    p = Booking.objects.get(id=p)
    p.delete()
    return render(request, 'bookinglist.html')

def customreg(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        m = request.POST['m']
        a = request.POST['a']
        if p == cp:
            u = CustomUser.objects.create_user(username=u, password=p, email=e, phone=m, address=a)
            u.is_customer = True
            u.save()
            return redirect('home')
        else:
            return HttpResponse("Password not matching")
    return render(request,'customerregister.html')

def serviceproviderreg(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        m = request.POST['m']
        a = request.POST['a']
        if p == cp:
            u = CustomUser.objects.create_user(username=u, password=p, email=e, phone=m, address=a)
            u.is_serviceprovider = True
            u.save()
            return redirect('home')
        else:
            return HttpResponse("Password not matching")
    return render(request,'serviceproviderregister.html')

def adminreg(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        m = request.POST['m']
        a = request.POST['a']
        if p == cp:
            u = CustomUser.objects.create_user(username=u, password=p, email=e, phone=m, address=a)
            u.is_admin = True
            u.save()
            return redirect('home')
        else:
            return HttpResponse("Password not matching")
    return render(request,'adminregister.html')


def user_login(request):
    if (request.method=="POST"):
        name = request.POST['u']
        pass1 = request.POST['p']
        user = authenticate(username=name,password=pass1)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'customerlogin.html')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('home')

def addcategory(request):
    form = Categoryform()
    if (request.method=="POST"):
        form = Categoryform(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request, 'addcategory.html',{"form":form})

def empdetail(request):
    e = CustomUser.objects.filter(is_serviceprovider=True)
    return render(request, 'empdetail.html',{"e":e})

def viewcategory(request):
    v = Category.objects.all()
    return render(request, 'viewcategory.html', {"v":v})

def editcategory(request,p):
    c = Category.objects.get(id=p)
    form = Categoryform(instance=c)
    if(request.method=="POST"):
        form = Categoryform(request.POST,request.FILES,instance=c)
        if form.is_valid():
            form.save()
            return viewcategory(request)
    return render(request, 'addcategory.html',{"form":form})

def deletecategory(request,p):
    p = Category.objects.get(id=p)
    p.delete()
    return render(request,'viewcategory.html')





