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



    

