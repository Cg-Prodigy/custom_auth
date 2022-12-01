from django.urls import path
from .views import signUpPage,loginPage,homePage,logoutUser,validate_input
urlpatterns = [
    path("",homePage,name="homepage"),
    path("signup/",signUpPage,name="signup"),
    path("login/",loginPage,name="login"),
    path("logout/",logoutUser,name="signout"),
    path("validate_input/",validate_input,name="validate_input"),
]


