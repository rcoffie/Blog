from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
  pass 


class Post(models.Model):
  status_choices = (
    ('draft','draft'),
    ('published','published'),
  )
  title = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body   = models.TextField()
  postImage = models.ImageField(upload_to='photos/%Y/%m/%d')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status   = models.CharField(max_length=15, choices=status_choices, default='draft', null=True)



  def __str__(self):
    return self.title