# imports dependencies
import requests
import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from crypto.forms import Signup
from crypto.models import PortfolioTracker

# view function for home page
def top100(request):
    api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C%2024h%2C7d'
    data = requests.get(api).json()

    # returns relevant data to home page table from the api endpoint above
    return render(request, template_name="top100.html", context={'coins':data})

# view function for home page
def index(request):
    return render(request, template_name="index.html")

# view function for registration
def registration(request):
    # the sign up form sends a post request
    if request.method == "POST":
        form = Signup(request.POST)
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
    form = Signup()
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

#  view funtion for portfolio
def view_portfolio(request):
    # autheticated user inputs are collected to return portfolio data based on the user input
    if request.user.is_authenticated:
        if request.method == 'POST':
            coin = request.POST.get('coin_name')
            symbol = request.POST.get('coin_symbol')
            token = request.POST.get('number_tokens')
            # when a coin name is recieved a portfolio object is created based on the users input
            if coin:
                PortfolioTracker.objects.create(
                                                user=request.user, crypto=coin,
                                                symbol=symbol, tokens=token)
                messages.info(request, f"{token} {coin} was added to your portfolio.")
                # user returned to the same page (portfolio) so that they can view their portfolio data
                return HttpResponseRedirect(reverse("portfolio"))

        #  lists values are empty
        else:
            portfolio_objs = PortfolioTracker.objects.filter(user=request.user)
            name_list = []
            value_list = []
            day_list =[]
            week_list =[]
            hour_list =[]
            year_list =[]
            highs_list =[]
            lows_list =[]

            #  user coin input is added to api data to populate lists
            for objs in portfolio_objs:
                url = f'https://api.coingecko.com/api/v3/coins/{objs.crypto}'
                data = requests.get(url).json()

                float_currency_amount = float(objs.tokens)
                price = data['market_data']['current_price']['usd']
                day= data['market_data']['price_change_percentage_24h_in_currency']['usd']
                week= data['market_data']['price_change_percentage_7d_in_currency']['usd']
                hour= data['market_data']['price_change_percentage_1h_in_currency']['usd']
                year= data['market_data']['price_change_percentage_1y_in_currency']['usd']
                highs=data['market_data']['high_24h']['usd']
                lows=data['market_data']['low_24h']['usd']
                
                # users token(s) value is calculated in usd
                total_value = float_currency_amount * price
                # appends the collected data to the relvant list
                name_list.append(objs.crypto)
                value_list.append(total_value)
                day_list.append(day)
                week_list.append(week)
                hour_list.append(hour)
                year_list.append(year)
                highs_list.append(highs)
                lows_list.append(lows)
            #items are pared togteher and returned in the portfolio form
            complete_list = zip(name_list, value_list, day_list, week_list, hour_list, year_list,
            highs_list, lows_list)
            coin_data ={
                'datalist':complete_list
            }
            return render(request=request, template_name="portfolio.html" , context=coin_data)
    else:
        return render(request=request, template_name="portfolio.html")

