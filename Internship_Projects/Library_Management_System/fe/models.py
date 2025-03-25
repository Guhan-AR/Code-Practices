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