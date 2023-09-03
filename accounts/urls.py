from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='Login'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('profile/', edit_profile, name='Profile'),
    path('', include('django.contrib.auth.urls')) #Contains urls for login and out
]