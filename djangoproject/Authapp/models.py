from django.db import models
from django.utils import timezone
class userModel(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='Image/')
    date_create=models.DateTimeField(default=timezone.now)
    description=models.TextField(default='')
    def __str__(self):
        return self.username
class Product(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField()
    stocks=models.IntegerField()
    
    def __str__(self):
        return self.name