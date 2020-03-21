from django.shortcuts import render,redirect
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from .import models

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        email2 = request.POST['email2']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = request.POST['username']
        company_name = request.POST['company_name']
        if email != email2:
            return
        if password != password2:
            return
        if len(password)<8:
            return
        myuser = models.MyUser.objects.create_user(email=email, username=username, password=password)
        myuser.save()
        new_account_user = models.Account(user=myuser,company_name=company_name)
        new_account_user.save();
        return redirect('login')
    return render(request,"account/register.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
    return render(request, "account/login.html")


def logout(request):
      auth.logout(request)
      return redirect('login')
      
