from django.urls import path
from .views import signUpPage,loginPage,homePage,logoutUser
urlpatterns = [
    path("",homePage,name="homepage"),
    path("signup/",signUpPage,name="signup"),
    path("login/",loginPage,name="login"),
    path("logout/",logoutUser,name="signout"),
]
