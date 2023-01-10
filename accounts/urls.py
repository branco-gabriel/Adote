from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.log_out, name='log_out'),
 
]