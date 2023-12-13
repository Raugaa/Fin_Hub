from django.db import models
from django.contrib.auth.models import *

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
