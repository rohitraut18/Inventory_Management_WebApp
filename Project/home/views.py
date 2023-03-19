from curses.ascii import HT
from pickle import NONE
from django.shortcuts import render,  redirect
# from home.models import Contact
from django.contrib import messages
# from .forms import UserRegistrationForm
from home.forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import  render, redirect
# from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from home.forms import InventoryForm  
from home.models import Inventory  


# Create your views here.
def home(request):
    return render(request, 'home.html')

def joinaction(request):
    if (request.method == 'POST'):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            print("Rohit....................................")
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('loginaction')
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'join.html', page_data)
    else:
        join_form = JoinForm()
        context = {'join_form': join_form}
        print("hey")
        return render(request, 'join.html', context)

def loginaction(request):
    if (request.method == "POST"):
        login_form = LoginForm(request.POST)
        if (login_form.is_valid()):
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as " + username)
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
                return render(request, 'login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {"login_form": LoginForm})

@login_required
def logoutaction(request):
    logout(request)
    return redirect("home")


def about(request):
    return render(request, 'about.html')

@login_required
def emp(request):  
    if request.method == "POST": 
        form = InventoryForm(request.POST,  request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = InventoryForm()  
    return render(request,'index.html',{'form':form})  

@login_required
def show(request):  
    inventories = Inventory.objects.all()  
    return render(request,"show.html",{'inventories':inventories})  

@login_required
def edit(request, id):  
    inventory = Inventory.objects.get(id=id)  
    return render(request,'edit.html', {'inventory':inventory})  

@login_required
def update(request, id):  
    inventory = Inventory.objects.get(id=id)  
    form = InventoryForm(request.POST, request.FILES, instance = inventory)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'inventory': inventory})  

@login_required
def destroy(request, id):  
    inventory = Inventory.objects.get(id=id)  
    inventory.delete()  
    return redirect("/show")  
