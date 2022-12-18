from django.test import TestCase, Client 
from posters.models import (Category, Author, Post, Comment)
import datetime


class TestModels(TestCase):
    
    def test_category_model(self):

        category = Category.objects.create(name='Category example')
        self.assertEqual(str(category), 'Category example')
    

    def test_post_and_comment_model(self):

        data = {
            'title' : 'testing title',
            'description' : 'title description',
            'content' : 'lorem ipsum lorem ipsum',
            'address' : 'address example',
            'status' : 2,
            'updated_at' : datetime.datetime.now(),
            'longitude' : 20,
            'latitude': 20,
        }
        post = Post.objects.create(**data)
        self.assertEqual(str(post), 'testing title')
        self.assertEquals(post.get_latitude_longitude(), (20, 20))
        comment = Comment.objects.create(post=post, comment='Example Comment')
        self.assertEqual(str(comment), 'Example Comment')
    
    def test_author_model(self):
        
        #There are in our tasks
        pass
        