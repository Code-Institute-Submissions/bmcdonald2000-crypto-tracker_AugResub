# imports django path, django admin and view funtions
from django.contrib import admin
from django.urls import path
from crypto.views import index, registration, Userlogin, view_portfolio
from crypto.views import log_out, top100

# sets out the path for the relevant templates
urlpatterns = [
   path('', index, name='home'),
   path('admin/', admin.site.urls),
   path('Registration', registration, name='registration'),
   path('Login', Userlogin, name='userlogin'),
   path('Logout', log_out, name='logout'),
   path('Portfolio', view_portfolio, name='portfolio'),
   path('Top 100', top100, name='top100'),
]
