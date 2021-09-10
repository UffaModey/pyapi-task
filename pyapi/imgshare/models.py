from django.db import models

# Create your models here.
class Posts(models.Model):
    imageurl = models.CharField(max_length=150)
    caption = models.CharField(max_length=100)
    likes = models.IntegerField()
    
    def __str__(self):
        return self.imageurl

class Users(models.Model):
    username = models.CharField(max_length=100)
    following = models.CharField(max_length=100)
    followers = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
