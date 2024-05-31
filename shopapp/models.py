
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name
    
    
genderchoices = [
    ('male', "Male"),
    ('female', "Female"),
    ]

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender= models.CharField(max_length=100,choices=genderchoices,default='male')
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    # password=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    stock = models.PositiveIntegerField()
    sales = models.PositiveIntegerField(default=0)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.product.name}"



