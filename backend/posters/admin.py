from django.contrib import admin
from .models import (Category, Post, Author, Comment)

models = (Category, Post, Author, Comment)
for model in models:
    admin.site.register(model)