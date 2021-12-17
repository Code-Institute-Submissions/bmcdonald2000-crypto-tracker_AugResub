# inports django models and user
from django.db import models
from django.contrib.auth.models import User
 
# Creates model
class PortfolioTracker(models.Model):
   user = models.ForeignKey(to=User, on_delete=models.CASCADE)
   crypto = models.CharField(max_length=100)
   symbol = models.CharField(max_length=20, default=None)
   tokens = models.CharField(max_length=50 , default=None, null=True, blank=True)
 
   def __str__(self):
       return str(self.crypto)
