from django.db import models

class Color(models.Model):

    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Person(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey(Color,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
