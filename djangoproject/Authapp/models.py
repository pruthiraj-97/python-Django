from django.db import models
from django.utils import timezone
# Create your models here.
class userModel(models.Model):
    USERS_TYPES=[
        ('AD','ADMIN'),
        ('US','USER'),
        ('OW','OWNER')
    ]
    name=models.CharField(max_length=100)
    password=models.CharField()
    image=models.ImageField(upload_to='images/')
    add_date=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=USERS_TYPES)
    
