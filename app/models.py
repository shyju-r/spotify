from django.db import models

# Create your models here.
class Signupmodel(models.Model):
    email=models.EmailField()
    password=models.TextField()
    
    
class IndexModel(models.Model):
    image=models.ImageField(upload_to="images",null=True)
    imagename=models.TextField(null=True)
    imagedetails=models.TextField(null=True)
    status=models.BooleanField(default=False)