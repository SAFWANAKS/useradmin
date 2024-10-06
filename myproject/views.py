from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *

def index(request):
    return render(request,'index.html')
def first(request):
    return render(request,'index.html')
   
def userreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(myfile.name,myfile)
        reg=userdetails(name=name,phone=phone,email=email,password=password,image=myfile)
        reg.save()
        return redirect(userlogin)
    return render(request,'register.html',{'success':'Registered successfully'})

def viewuser(request):
    users=userdetails.objects.all()
    return render(request,'userview.html',{'result':users})
    

def usercontact(request):
    a=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        file=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(file.name,file)
        reg=contactdetails(name=name,phone=phone,email=email,image=file,userid=a)
        reg.save()
        return redirect(viewcontact)
    return render(request,'contact.html',{'success':'contact added successfully'})
    

def viewcontact(request):
    t=request.session['uid']
    user=contactdetails.objects.filter(userid=t)
    return render(request,'usercontactview.html',{'result':user})
    
def userlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email== 'admin@gmail.com' and password == 'admin':
        request.session['logindetails'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif userdetails.objects.filter(email=email,password=password).exists():
        users=userdetails.objects.get(email=request.POST['email'],password=password)
        if users.password == request.POST['password']:
                request.session['uid']=users.id
                request.session['uname']=users.email
                request.session['email']= email
                request.session['user'] = 'user'
                return render(request,'index.html')
    else:
        return render(request,'login.html',{'success':'User login successfully'})   

def logout(request):
    session_keys = list(request.session.keys()) 
    for key in session_keys:
        del request.session[key]
    return redirect(index)  

def viewprofile(request):
    tem=request.session['uid']
    vpro=userdetails.objects.get(id=tem)
    return render(request,'profileview.html',{'result':vpro})   

def adminprofile(request):
    return render(request,'adminprofile.html')   


def delete(request,id):
    member = contactdetails.objects.get(id=id)
    member.delete()
    return redirect(viewcontact)
  
def dele(request,id):
    member = userdetails.objects.get(id=id)
    member.delete()
    return redirect(viewuser)

def update(request,id):
    member= userdetails.objects.get(id=id)
    return render(request,'profileupdate.html',{'result':member}) 

def upt(request,id):
     if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(myfile.name,myfile)
        reg=userdetails(name=name,phone=phone,email=email,password=password,image=myfile,id=id)
        reg.save()
        return redirect(viewprofile)

def change(request,id):
    member= contactdetails.objects.get(id=id)
    return render(request,'contactupdate.html',{'result':member}) 

def ch(request,id):
    a=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(myfile.name,myfile)
        reg=contactdetails(name=name,phone=phone,email=email,image=myfile,userid=a,id=id)
        reg.save()
        return redirect(viewcontact)