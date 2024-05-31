from django.urls import path
from Authapp import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('allusers/',views.all_users,name='all_users'),
    path('product/',views.All_Products,name='All_Produts'),
]