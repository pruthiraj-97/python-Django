from django.urls import path
from Authapp import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login')
]