from django.urls import path
from djangoapp import views

urlpatterns = [
    path('alllanguage/',views.all_language,name='all_language'),
]