from django.db import models

class category(models.Model):
    name= models.CharField(max_length=20)
    descritpion=models.TextField()
    image=models.ImageField(upload_to='Shop/categories', blank=True, null=True)

    def __str__(self):
        return self.name


class product(models.Model):
    name= models.CharField(max_length=20)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Shop/products', blank=True, null=True)
    description= models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



