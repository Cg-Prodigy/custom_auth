from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RentUser,HouseModel

class RentUserForm(UserCreationForm):
    class Meta:
        model=RentUser
        fields=("nat_id","first_name","last_name","email","dob","user_type","password1","password2")
        widgets={
            "dob":forms.DateInput(attrs={'type':'date'}),
            "email":forms.EmailInput(attrs={"placeholder":"Working Email Address"}),
        }
class HouseForm(forms.ModelForm):
    class Meta:
        model=HouseModel
        fields="__all__"
        exclude=("landlord",)