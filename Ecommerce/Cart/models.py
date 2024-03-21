from django.db import models
from Shop.models import product
from django.contrib.auth.models import User

class cart(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product.name

    def subtotal(self):
        return self.quantity*self.Product.price



class Order(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20, default="pending")
    delivery_status = models.CharField(max_length=20, default="pending")
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Account(models.Model):
    accnum = models.CharField(max_length=20)
    acctype = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return self.accnum







