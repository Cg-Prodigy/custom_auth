from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import RentUserForm,HouseForm
from .models import HouseModel
# Create your views here.

def homePage(request):
    houses=HouseModel.objects.all()
    return render(request,"index.html",{"houses":houses})

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

def houseView(request):
    if request.method=="POST":
        form=HouseForm(request.POST)
        if form.is_valid():
            house=form.cleaned_data["house_name"]
            form=form.save(commit=False)
            form.landlord=request.user
            form.save()
            messages.success(request,f"{house} has been registered successfully")
            return redirect("house_reg")
    else:
        form=HouseForm()
    return render(request,"custom/house.html",{"form":form})

def houseDetails(request,pk):
    house=get_object_or_404(HouseModel,id=pk)
    return render(request,"custom/house_det.html",{"house":house})
# htmx

def validate_input(request):
    return HttpResponse(None)
    