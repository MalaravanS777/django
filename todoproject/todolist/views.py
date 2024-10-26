from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib import messages
from django.apps import apps
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
# Create your views here.
@never_cache
def todo(request):
    logout(request)
    request.session['sname']=None
    return render(request, 'index.html')
    
def signupinfo(request):
    try:
        email=request.POST.get('email')
        passw=request.POST.get('pass')
        c=credentials(email=email,passw=passw)
        c.save()
        message=["you have signed up successfully......","Now you can login using the same mail id and password......"]
        for m in message:
            messages.success(request,m)
        try:
            tb=email.split("@")[0]
            create_table.create(tb)
            print("created successfully....")
        except Exception as e:

            print(e,"unsuccessful")
        return render(request,'login.html')
    except:
        message=["Email id already exist....","Use different mail id....","Otherwise try to login using the same mail id by clicking below login....."]
        for m in message:
            messages.error(request,m)
        return render(request,'signup.html')
def si(request):
    return render(request,'signup.html')
def li(request):
    return render(request,'login.html')
def logindetails(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    c=credentials.objects.filter(email=email)
    tb=email.split("@")[0]
    if c.exists():
        cs=credentials.objects.filter(email=email,passw=passw)
        if(cs.exists()):
            row=fetch_rows(tb)
            request.session['sname']=tb
            
            res={
                'data':row
            }
            print(res)
            return render(request,'todolist.html',res)
        else:
            messages.error(request,"The password is incorrect....")
            return render(request,"login.html")
    else:
        message=["Email does not exist....","Please enter the registered email.... OR First sign up and then try again..."]
        for m in message:
            messages.error(request,m)
        return render(request,'login.html')

def insert(request):
    if(request.method=='POST'):
        tb=request.session.get('sname')
        print(tb)
        task=request.POST.get('work')
        insert_task(tb,task)
        data=fetch_rows(tb)
        res={'data':data}
        return render(request,'todolist.html',res)

def delete(request):
    tb=request.session.get('sname')
    id=request.POST.get('id')
    delete_task(tb,id)
    data=fetch_rows(tb)
    res={'data':data}
    return render(request,'todolist.html',res)

def update(request):
    tb=request.session.get('sname')
    id=request.POST.get('id')
    task=request.POST.get('work')
    dict={'id':id,'task':task}
    return render(request,'update.html',dict)

def update_con(request):
    tb=request.session.get('sname')
    id=request.POST.get('id')
    task=request.POST.get('work')
    update_task(tb,id,task)
    data=fetch_rows(tb)
    res={'data':data}
    return render(request,'todolist.html',res)

    