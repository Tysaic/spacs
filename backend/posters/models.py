from django.db import models
from django.contrib.auth.models import User 
from django.utils.functional import lazy

status_post = (
    ('1', 'Abierto'),
    ('2', 'Cerrado')
)

class Category(models.Model):
    name = models.CharField('Category:', max_length = 32)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    # Setting plural name to django admin panel
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.IntegerField()


    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 255)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    address = models.CharField(max_length = 255, null=True)
    status = models.CharField(max_length = 32, choices = status_post, default='1')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length = 255)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(null=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment
