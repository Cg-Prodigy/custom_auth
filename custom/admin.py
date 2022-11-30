from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import RentUser
# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=RentUser
        fields=("nat_id","first_name","last_name","email","dob","user_type")
        widgets={
            "dob":forms.DateInput(attrs={"type":"date"})
        }
    def clean_password2(self):
        pswd1=self.cleaned_data.get("password1")
        pswd2=self.cleaned_data.get("password2")
        if pswd1 and pswd2 and pswd1!=pswd2:
            raise ValidationError("Password mismatch")
        return pswd2
    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=RentUser
        fields=("nat_id","first_name","last_name","email","dob","user_type","is_admin","is_active")

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=("nat_id","first_name","last_name","email","dob")
    list_filter=("is_admin",)
    add_fieldsets=(
        (None,{
            "classes":("wide",),
            "fields":("nat_id","first_name","last_name","email","dob","user_type","password1","password2")
        })
    )
    search_fields=("nat_id",)
    ordering=("nat_id",)
    filter_horizontal=()

admin.site.register(RentUser,UserAdmin)
admin.site.unregister(Group)