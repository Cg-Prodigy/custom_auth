from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import RentUserForm
# Create your views here.

def homePage(request):
    return render(request,"index.html")

def signUpPage(request):
    if request.method=="POST":
        form=RentUserForm(request.POST)
        if form.is_valid():
            f_name=form.cleaned_data['first_name']
            form.save()
            messages.success(request,f"Account for {f_name} has been created succesfully.")
            return redirect("login")
    else:
        form=RentUserForm()
    return render(request,"custom/signup.html",{'form':form})

def loginPage(request):
    if request.method=="POST":
        nat_id=request.POST.get("nat_id")
        pswd=request.POST.get("password")
        print(nat_id,pswd)
        user=authenticate(request,username=nat_id,password=pswd)
        if user:
            login(request,user)
            return redirect("homepage")
        else:
            messages.info(request,"Incorrect National Id or password!")
    return render(request,"custom/login.html")

def logoutUser(request):
    logout(request)
    return redirect("homepage")