from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image =  models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
