# imports dependencies
from django.contrib import admin
from crypto.models import PortfolioTracker
 
# Registers model portfolioTracker in the admin panel
admin.site.register(PortfolioTracker)