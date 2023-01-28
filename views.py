from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from studentapp.models import City, Course, student


# Create your views here.

@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def register_fun(request):  # '''it will be redirect to register.html page'''

    return render(request, 'register.html', {'data': ''})


@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def regdata_fun(request):
    user_name = request.POST['txtnm']
    user_email = request.POST['txtem']
    user_pswd = request.POST['txtpa']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():

        return render(request, 'register.html', {'data': 'Username,email and password is already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_pswd)
        u1.save()
        return redirect('log')


@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def log_fun(request):

    return render(request, 'login.html',{'data':''})


@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def logdata_fun(request):
    user_name = request.POST['txtnm']
    user_pswd = request.POST['txtpa']
    user1=authenticate(username=user_name, password=user_pswd)#it will compare the user table,,,,this function is
    # used to only user table not for all tables
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not superuser'})
    else:
        return render(request, 'login.html', {'data': 'Enter proper username and password'})

@login_required
@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required # not no redirect to other pages inside home page without logging in
@cache_control(no_cache=True,revalidate=True,nostere=True) # not no redirect to back
@never_cache
def add_student_fun(request):
    city=City.objects.all()
    course=Course.objects.all()
    return render(request, 'add students.html',{'City_data':city,'Course_data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def adddata_fun(request):
    s1 = student()
    s1.Student_Name = request.POST['txtnm']
    s1.Student_Age = request.POST['txtag']
    s1.Student_Phno = request.POST['txtph']
    s1.Student_City = City.objects.get(City_Name=request.POST['ddlCity'])
    s1.Student_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
    s1.save()
    return redirect('add')
    # return redirect(request,'add students.html',{'data':'student data inserted successfully'})


@login_required
@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def display_fun(request):
    s1 = student.objects.all()
    return render(request,'display.html',{'data':s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def update_fun(request,id):
    s1 = student.objects.get(id=id)
    city= City.objects.all()
    course=Course.objects.all()

    if request.method == 'POST':
        s1.Student_Name = request.POST['txtnm']
        s1.Student_Age = request.POST['txtag']
        s1.Student_Phno = request.POST['txtph']
        s1.Student_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Student_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()

        return redirect('display')

    return render(request,'update.html',{'data':s1,'Student_City':city,'Student_Course':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache
def delete_fun(request,id):
    s1 = student.objects.get(id=id)
    s1.delete()
    return redirect('display')

@cache_control(no_cache=True,revalidate=True,nostere=True)
@never_cache

def log_out_fun(request):

    logout(request)

    return redirect('log')