from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Supplier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.company_name

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_pics/')
    contact_details = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"notification for {self.user.username}" 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"