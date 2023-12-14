from django.db import models
from django.contrib.auth.models import *

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = 'Clients')

class FreeLancer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worktype = models.TextField(null = True, blank = True)
    exp = models.IntegerField(null = True, blank = True)
    edu = models.TextField(null = True, blank = True)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = 'FL_PP')
    workdesc = models.TextField(null = True, blank = True)
    desc = models.TextField(null = True, blank = True)
    qual = models.TextField(null = True, blank = True)

class pastprojects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(null = True, blank = True)
    img = models.ImageField(null = True, blank = True, upload_to = 'PP')
    title = models.CharField(null = True, blank = True, max_length = 500)

class req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(null = True, blank = True)
    img = models.ImageField(null = True, blank = True, upload_to = 'req')
    title = models.CharField(null = True, blank = True, max_length=500)





# Create your models here.
