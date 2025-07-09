from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40,null=True)
    mobile = models.CharField(max_length=20,null=False,blank=False,unique=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Product_Type(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Product(models.Model):
    name=models.CharField(max_length=400)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.TextField(max_length=5000)
    d_price = models.PositiveIntegerField(default=200)
    category = models.ForeignKey(Product_Type,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.name

class Comment(models.Model):

    name=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    comment=models.TextField()
    date= models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Product_Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_image/multi/',null=True,blank=True)

    def __str__(self):
        return f'Image for {self.product.name}'

class OfferBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offer_banner/',null=True,blank=True)

    def __str__(self):
        return self.title
    
class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name