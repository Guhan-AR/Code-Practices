from django.db import models

class Product_db(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.name