# imports dependencies
import requests
import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from crypto.forms import signup
from crypto.models import PortfolioTracker
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm


# view function for home page
def index(request):
   api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C%2024h%2C7d'
   data = requests.get(api).json()
 
 # returns relevant data to home page table from the api endpoint above
   return render(request, template_name="index.html", context={'coins':data})

# view function for registration
def registration(request):
    # the sign up form sends a post request
    if request.method == "POST":
            form = signup(request.POST)
             # if the form is valid, it's saved an user is notified
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("registration")
            else:
                 # if the form is invalid user is notfied and registration attempt is not saved
                messages.error(request, "Registration unsuccessful. Please fill out the form correctly")
    # the signup form from forms.py 
    form = signup()
     #  http respone is then retured to the browser
    return render (request=request, template_name="registration.html", context={"form":form})
#  view function for login, django authentication form is used
def Userlogin(request):
    if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            #  valid form clears form inputs
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                #  user is notified once successfully logged in
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("userlogin")
                else:
                    #  if login is uncessful user is notified
                    messages.error(request,"Incorrect username or password, please try again.")
            else:
                messages.error(request,"Invalid username or password,please try again.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login":form})
#  view funtion for logging out
def log_out(request):
    #  django logout is used and user notified once they log out sucessfully
    logout(request)
    messages.info(request, "You have successfully logged out.")  
    #  user is then redirected to the login page
    return redirect("userlogin")
    return render(request=request, template_name='logout.html')





    

