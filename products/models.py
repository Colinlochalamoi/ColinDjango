from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length= 255)
  pub_date = models.DateField(default=datetime.date.today)
  body = models.TextField()
  url = models.TextField()
  image = models.ImageField(upload_to='images/')
  icon = models.ImageField(upload_to = 'images/')
  votes = models.IntegerField(default=1)
  hunter = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
  return self.title

def summary(self): 
  return self.body[:100]

def pub_date_nice(self): 
  return self.pub_date.strtime('%b %e %Y')