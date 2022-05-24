# imports django path
from django.urls import path, include


# sets out the path for admin and links crypto app urls
urlpatterns = [
   path('', include('crypto.urls')),

]
