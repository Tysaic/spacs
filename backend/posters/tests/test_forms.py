from django.test import TestCase
from posters.forms import (
    PostForm, 
    CategoryForm, 
    CommentForm, 
    GeoLocatorForm
)

from posters.models import Post
import datetime

class TestForm(TestCase):

    def setUp(self):
        self.data_post = {
            'title' : 'testing title',
            'description' : 'title description',
            'content' : 'lorem ipsum lorem ipsum',
            'address' : 'address example',
            'status' : 2,
            'updated_at' : datetime.datetime.now(),
            'longitude' : 20,
            'latitude': 20,
        }
 
    def test_post_form_is_valid(self):

        data = self.data_post
        form = PostForm(data)

        self.assertTrue(form.is_valid())
    
    def test_post_no_data(self):

        data = {}

        form = PostForm(data)

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
    
    def test_category_is_valid(self):

        data = {'name': 'Category Testing'}
        form = CategoryForm(data)
        self.assertTrue(form.is_valid())
    
    def test_category_no_data(self):

        data = {}
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
    
    def test_comment_is_valid(self):

        post = Post.objects.create(**self.data_post)
        form = CommentForm(
            {'comment': 'Comment here'}
        )
        self.assertTrue(form.is_valid())
    
    def test_category_no_data(self):

        data = {}
        form = CommentForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
 