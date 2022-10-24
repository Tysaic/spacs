from django.db import models
from django.contrib.auth.models import User 


class Category(models.Model):
    name = models.CharField(max_length = 32)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 255)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
    comment = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
