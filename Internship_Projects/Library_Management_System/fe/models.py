from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=100 , null=True)
    book_author = models.CharField(max_length=100 , null=True)
    about_book = models.TextField(null=True)
    book_price = models.IntegerField(default=0)
    book_image = models.FileField(null=True)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title

class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone_no = models.DecimalField(decimal_places=0,max_digits=10)
    mail = models.EmailField()

    def __str__(self):
        return self.name

# CharacterField
# integerField
# floatField
# decimalfield
# datefield
# timefield
# datetimefield
# textfield
# booleanfield
# emailfield
# imagefiled
# filefield
# urlfield
# foreignkey
# ontotoonefield
# manytomanyfield
# positiveintegerfield
