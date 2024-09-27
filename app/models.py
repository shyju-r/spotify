from django.db import models
import string
import random

# Create your models here.
class Signupmodel(models.Model):
    email=models.EmailField()
    password=models.TextField()
    
class CategoryModel(models.Model):
    category_name=models.TextField(null=True)
  

class Subcategorymodel(models.Model):
    
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    category_name=models.TextField(null=True)
    playlistimage=models.ImageField(upload_to="images")
    playlistname=models.TextField()
    playlistartists=models.TextField()
    
def generate_Id(length=8):
    characters = string.ascii_uppercase + string.digits
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid
    
class Songmodel(models.Model):
    palylist=models.ForeignKey(Subcategorymodel,on_delete=models.CASCADE,null=True)
    playlistname=models.TextField(null=True)
    number=models.TextField()
    songimage=models.ImageField(upload_to="images")
    songname=models.TextField()
    songartist=models.TextField()
    moviename=models.TextField()
    plays=models.TextField()
    duration=models.TextField()
    song = models.FileField(upload_to="audio_files/",null=True) 
    trans_Id = models.CharField(null=True, max_length=8, unique=True, blank=True )
    
    def save(self, *args, **kwargs):
        if not self.trans_Id:
            self.trans_Id = generate_Id()
        super(Songmodel,self).save(*args, **kwargs)