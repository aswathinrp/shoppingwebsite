from django.db import models

# Create your models here.
class dress(models.Model):
    name =models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    price=models.IntegerField()
