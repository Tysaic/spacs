from unicodedata import category
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime 
from .models import (Post, Category)
from .forms import (PostForm, CategoryForm)
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def list_post(request):

    template = 'posters/list_post.html'
    data = {'posts' : Post.objects.all()}
    return render(request, template, data)

def create_post(request):
    context = {}
    template = 'posters/create_post.html'
    post_form = PostForm(request.POST or None)
    category_form = CategoryForm(request.POST or None)

    if post_form.is_valid() and category_form.is_valid():
        #Save category post here
        post = post_form.save()
        category = Category.objects.get_or_create(**category_form.cleaned_data)[0]
        post_to_category = Post.objects.get(id = post.id)
        post_to_category.category = category
        post_to_category.save()
        return HttpResponse('<h1>Created Post</h1>')

    context['post_form'] = post_form
    context['category_form'] = category_form

    return render(request, template, context=context)

def edit_post(request, pk):
    context = {}
    template = 'posters/edit_post.html'
    post_to_edit = get_object_or_404(Post, id = pk)
    form = PostForm(request.POST or None, instance=post_to_edit)

    #post_to_edit = Post.objects.filter(pk=pk)

    if form.is_valid():
        post_to_edit.title = form.cleaned_data['title']
        post_to_edit.description = form.cleaned_data['description']
        post_to_edit.content = form.cleaned_data['content']
        post_to_edit.updated_at = datetime.datetime.now()
        post_to_edit.status = form.cleaned_data['status']
        post_to_edit.save()
        data = {'message': 'Post loaded succesfully'}
        return render(
            request, 
            'posters/succesfully.html', 
            data 
        )
    
    context['form'] = form 
    context['created_at'] = post_to_edit.created_at
    context['updated_at'] = post_to_edit.updated_at

    return render(request, template, context=context)

def delete_post(request, pk):
    template = 'posters/succesfully.html', 
    post_to_delete = get_object_or_404(Post, id = pk)
    post_to_delete.delete()
    data = {'message': 'Post deleted succesfully'}
    return render(request, template, data)

