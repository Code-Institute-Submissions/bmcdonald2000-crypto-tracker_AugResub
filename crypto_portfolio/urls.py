# imports django path, django admin and funtion names
from django.contrib import admin
from django.urls import path
from crypto.views import index, registration, Userlogin, view_portfolio, log_out

# sets out the path for the relevant templates
urlpatterns = [
   path('', index, name='index'),
   path('Templates/registration.html', registration, name='registration'),
   path('Templates/login.html', Userlogin, name='userlogin'),
   path('Templates/index.html', index, name='home'),
   path('Templates/logout.html', log_out, name='logout'),
   path('Templates/portfolio.html', view_portfolio, name='portfolio'),
]

