from enum import auto
from django.http import request
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,Contribute,Joinus
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout

# Create your views here.

def home(request):
    return render(request,"home.html")



def cont(request):
    if request.method =='POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         issue=request.POST.get('issue')
         contact=Contact(name=name,email=email,issue=issue,date=datetime.today())
         contact.save()
         messages.success(request,'Your response recorded')

   
    return render(request,"contact.html")

def services(request):
    return render(request,"service.html")



def contribute(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        contribution=request.POST.get('contribution')
        center=request.POST.get('center')
        contrib=Contribute(name=name,email=email,contact=contact,contribution=contribution,center=center,date=datetime.today())
        contrib.save()
        

    return render(request,"contribute.html")

def join(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        reason=request.POST.get('reason')
        state=request.POST.get('state')
        city=request.POST.get('city')
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        occupation=request.POST.get('occupation')
        Join=Joinus(name=name,email=email,contact=contact,reason=reason,state=state,city=city,DOB=DOB,occupation=occupation,gender=gender,Request_date=datetime.today())
        Join.save()

    return render(request,"join.html")

def overview(request):
    return render(request,"overview.html")

def team(request):
    return render(request,"team.html")

def awards(request):
    return render(request,"awards.html")

def vision(request):
    return render(request,"vision.html")

def founder(request):
    return render(request,"founder.html")




def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            number = request.POST['number']
            passw = request.POST['password']
            cpassw = request.POST['cpassword']

            if len(number) != 10:
                messages.error(request,"Mobile Number Should Be 10 Digit")
                return redirect('/signup')
            
            elif passw != cpassw:
                messages.error(request,"Password And Confirm Password Should Be Same")
                return redirect("/signup")
            
            else:
                email_check = User.objects.filter(email=email)
                number_check = User.objects.filter(username=number)
                
                if len(email_check) != 0:
                    messages.error(request,"Your Email is Already Exists")
                    return redirect('/signup')
                
                elif len(number_check) != 0:
                    messages.error(request,"Your Numer is Already Exists")
                    return redirect('/signup')

                else:
                    obj = User.objects.create_user(number,email,cpassw)
                    obj.first_name = fname
                    obj.last_name = lname
                    obj.save()
                    messages.success(request,"Your Account Created Successfully.")
                    return redirect('/')     


        return render(request,"signup.html")
    return redirect('/')

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            number = request.POST['number']
            password = request.POST['password']

            if len(number) != 10:
                messages.error(request,"Mobile Number Should Be 10 Digit")
                return redirect('/login')

            user = authenticate(request,username=number,password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Sucessfully Login")
                return redirect('/')
            else:
                messages.error(request,"Your Username or Password is Not Valid")
                return redirect('/login')
        return render(request,'login.html')
    return redirect('/')

def logout(request):
    auth_logout(request)
    messages.success(request,"Sucessfully Logout")
    return redirect('/')

        

        




    return render(request,"login.html")