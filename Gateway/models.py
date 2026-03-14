from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [ ("PENDING", "Pending"), ("PAID", "Paid"),("FAILED", "Failed"),("CANCELLED", "Cancelled"),]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id}"
    
class Transaction(models.Model):
    STATUS_CHOICES = [ ("SUCCESS", "Success"), ("FAILED", "Failed"), ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    gateway = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField( max_length=20,choices=STATUS_CHOICES )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.transaction_id