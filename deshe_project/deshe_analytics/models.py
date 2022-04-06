from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# class User(AbstractUser):
#   username = None
#   email = models.EmailField(unique = True)
#   first_name = models.CharField(max_length = 100)
#   last_name = models.CharField(max_length = 100)
#   phone = models.CharField(max_length = 100, unique = True)
#   password = models.CharField(max_length=50)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['email', 'phone', 'password']
  
#   def __str__(self):
#       return "{}".format(self.email)

class Stock(models.Model):
    isin = models.CharField(max_length=100) 
    cid = models.IntegerField()
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    date = models.DateField()
    quarter = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    exchange = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
    marketcap = models.FloatField()

    def __str__(self):
      return "{}".format(self.country)

 