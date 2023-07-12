from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    phone_number = models.CharField(max_length=20 ,default="0000000000")
    address = models.CharField(max_length=100,default="address")

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
    

class Color(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    

    
class Size(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    

class FeaturedIn(models.Model):
    name=models.CharField(max_length=64)
    product=models.ManyToManyField('product',blank=True,related_name="product")

    def __str__(self):
        return f"{self.name}"



class product(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    title=models.CharField(max_length=64)
    img = models.ImageField(upload_to='app/images')
    price=models.FloatField()
    gender=models.CharField(max_length=64,choices=GENDER_CHOICES)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    color=models.ManyToManyField(Color)
    size=models.ManyToManyField(Size)
    
    def __str__(self):
        return f"{self.title}"
    


class comments(models.Model):
    comment=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="commentUser")
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True,related_name="commentProduct")

    def __str__(self):
        return f"{self.user} commented '{self.comment}' on {self.product}"
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="cartUser")
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True,related_name="cartProduct")
    color=models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True,related_name="cartColor")
    size=models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True,related_name="cartSize")
    quantity=models.IntegerField(default=1)
  
    
    def __str__(self):
        return f"{self.user} added {self.product} to cart"
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="wishlistUser")
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True,related_name="wishlistProduct")

    def __str__(self):
        return f"{self.user} added {self.product} to wishlist"
    


    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="orders")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default= datetime.now())
    statusChoices= [
        ('Pending', 'Pending'),
        ("accepted","accepted"),
        ("out for delivery","out for delivery"),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),

    ]
    status=models.CharField(max_length=64,default="Pending",choices=statusChoices)


    def __str__(self):
        return f"{self.user} placed an order with total {self.total}, STATUS: {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f" {self.order.user} ordered {self.product}"

 
    

