from django.db import models
from django.contrib.auth.models import User

class Venue_DB(models.Model):

    name = models.CharField('venue name',max_length=100)
    address = models.CharField('address',max_length=100)
    pin_code = models.CharField('pin code',max_length=15,blank=True)
    phone = models.CharField("phone number",max_length=15,blank=True)
    web = models.URLField("Website Address",blank=True)
    email_address = models.EmailField('EmailField',blank=True)

    def __str__(self):
        return self.name

class TurfUsers_DB(models.Model):
    first_name = models.CharField('first name',max_length=100)
    last_name = models.CharField('last name',max_length=100,blank=True)
    email = models.EmailField('user email',blank=True)

    def __str__(self):
        return self.first_name
    

class Event_DB(models.Model):

    name = models.CharField('event name',max_length=100)
    date = models.DateTimeField('event date')
    venue = models.ForeignKey(Venue_DB,blank=True,null = True,on_delete=models.CASCADE)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete = models.SET_NULL)
    description = models.TextField('game event description',blank=True)
    attendees = models.ManyToManyField(TurfUsers_DB,blank=True)

    def __str__(self):
        return self.name