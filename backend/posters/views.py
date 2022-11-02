from unicodedata import category
from urllib.request import HTTPRedirectHandler
from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime 
from .models import (Post, Category, Comment)
from .forms import (PostForm, CategoryForm, CommentForm)
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
    category_object = get_object_or_404(Category, id = post_to_edit.category.id)
    form = PostForm(request.POST or None, instance=post_to_edit)
    category_form = CategoryForm(request.POST or None, instance = category_object)

    #post_to_edit = Post.objects.filter(pk=pk)

    if form.is_valid() and category_form.is_valid():
        post_to_edit.title = form.cleaned_data['title']
        post_to_edit.description = form.cleaned_data['description']
        post_to_edit.content = form.cleaned_data['content']
        post_to_edit.updated_at = datetime.datetime.now()
        post_to_edit.status = form.cleaned_data['status']
        category_to_edit = Category.objects.get_or_create(**category_form.cleaned_data)[0]
        post_to_edit.category = category_to_edit
        post_to_edit.save()
        data = {'message': 'Post loaded succesfully'}
        return render(
            request, 
            'posters/succesfully.html', 
            data 
        )
    
    context['form'] = form 
    context['category_form'] = category_form
    context['created_at'] = post_to_edit.created_at
    context['updated_at'] = post_to_edit.updated_at

    return render(request, template, context=context)

def delete_post(request, pk):
    template = 'posters/succesfully.html', 
    post_to_delete = get_object_or_404(Post, id = pk)
    post_to_delete.delete()
    data = {'message': 'Post deleted succesfully'}
    return render(request, template, data)

def show_post(request, pk):
    template = 'posters/show_post.html'
    context = {}
    total_comments = []
    post_to_show = get_object_or_404(Post, id = pk)
    comments_by_post = Comment.objects.filter(post__id = pk)
    comment_form = CommentForm(request.POST or None)
    data_to_show = {
        'title': post_to_show.title, 
        'description': post_to_show.description,
        'content': post_to_show.content,
        #Author
        'category': post_to_show.category.name        
    }

    if comment_form.is_valid():
        user_comment = comment_form.save(commit=False)
        user_comment.status = 1
        user_comment.post = post_to_show
        user_comment.save()

    for comment in comments_by_post:

        total_comments.append({
            'comment': comment.comment,
            'created_at': comment.created_at,
        })

    context['data'] = data_to_show
    context['comments'] = total_comments
    context['comment_form'] = comment_form
    return render(request, template, context) 
