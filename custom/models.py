from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,nat_id,dob,user_type,password=None):
        if not nat_id:
            raise ValueError("User cannot sign up without valid ID")
        user=self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            nat_id=nat_id,
            dob=dob,
            user_type=user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,email,nat_id,dob,user_type,password=None):
        user= self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            nat_id=nat_id,
            dob=dob,
            user_type=user_type,
            password=password,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
class RentUser(AbstractBaseUser):
    USER_TYPE=(
        ("LD","Landlord"),
        ("TN","Tenant")
    )
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(verbose_name="Email Address",unique=True)
    nat_id=models.CharField(max_length=8,unique=True)
    dob=models.DateField(verbose_name="Date of Birth")
    user_type=models.CharField(choices=USER_TYPE,max_length=8)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD="nat_id"
    REQUIRED_FIELDS=["first_name","last_name","dob","user_type",'email']

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin