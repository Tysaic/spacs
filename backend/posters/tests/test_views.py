from django.test import TestCase, Client 
from django.urls import reverse, resolve
from posters.models import (Category, Author, Post, Comment)
from posters.views import (
    list_post, 
    create_post, 
    edit_post, 
    delete_post, 
    show_post,
    set_geolocator,
)
import json
import datetime


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.list_posters = reverse('list-posters')
        self.category_created_test = Category.objects.create(
            name = 'test_category_name'
        )
        self.post_created_test = Post.objects.create(
            title = 'Example Title',
            description='lorem ipsum',
            content = 'lorem ipsum ipsum',
            status = 1,
            latitude = 10,
            longitude = 10,
            category = self.category_created_test,
        )
        self.first_comment = Comment.objects.create(
            comment = 'First Comment',
            status = 1,
            post = self.post_created_test,
        )
        self.second_comment = Comment.objects.create(
            comment = 'Second Comment',
            status = 2,
            post = self.post_created_test,
        )
        self.post_pk = self.post_created_test.id
        self.show_post = reverse('show-post', args=[self.post_pk])
        self.create_post = reverse('create-post')
        self.edit_post = reverse('edit-post', args=[self.post_pk])
        self.delete_post = reverse('delete-post', kwargs={'pk': self.post_pk})
        self.data_to_post = {
            'title' : 'testing title',
            'description' : 'title description',
            'content' : 'lorem ipsum lorem ipsum',
            'address' : 'address example',
            'status' : 2,
            'updated_at' : datetime.datetime.now(),
            'name' : 'New category testing',
            'longitude' : 20,
            'latitude': 20,
        }
    
    def test_posters_list_GET(self):

        '''Just assert the status code and template'''
        response = self.client.get(self.list_posters)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters/list_post.html')
    
    def test_posters_show_without_comments_GET(self):

        '''
        Assert the status code, template and their comments
        '''
        response = self.client.get(self.show_post)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters/show_post.html')
        comments = response.context['comments']
        self.assertEquals(comments[0]['comment'], 'First Comment')
        self.assertEquals(comments[1]['comment'], 'Second Comment')


    
    def test_posters_show_with_comments_POST(self):
        
        '''
        Assert the status code, template and comment the post
        '''
        data = {
            'comment': 'New comment from testing'
        }
        response = self.client.post(self.show_post, data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters/show_post.html')
        new_comment = response.context['comments'][2]['comment']
        self.assertEquals(new_comment, data['comment'])

    
    def test_posters_create_post(self):
        '''
        Testing create post if there are the same values
        '''
        data = self.data_to_post
        response = self.client.post(self.create_post, data)
        self.assertEqual(response.status_code, 200)
        post = Post.objects.order_by('-id')[0]
        self.assertEquals(post.title, data['title'])
        self.assertEquals(post.description, data['description'])
        self.assertEquals(post.content, data['content'])
        self.assertEquals(post.address, data['address'])
        self.assertEqual(int(post.status), data['status'])
        updated_at = datetime.date(data['updated_at'].year, data['updated_at'].month, data['updated_at'].day)
        self.assertEquals(post.updated_at, updated_at)
        self.assertEquals(post.category.name, data['name'])

    
    def test_posters_edit_get(self):
 
        '''
        Just test the edit post as get method
        '''
        response = self.client.get(self.edit_post)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters/edit_post.html')

    def test_posters_edit_post(self):

        data = self.data_to_post

        '''
        Testing edit post if there are the same values sent to change.
        '''
        response = self.client.post(self.edit_post, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posters/succesfully.html')
        model_updated = Post.objects.get(pk=self.post_pk)
        self.assertEquals(model_updated.title, data['title'])
        self.assertEquals(model_updated.description, data['description'])
        self.assertEquals(model_updated.content, data['content'])
        self.assertEquals(model_updated.address, data['address'])
        self.assertEqual(int(model_updated.status), data['status'])
        updated_at = datetime.date(data['updated_at'].year, data['updated_at'].month, data['updated_at'].day)
        self.assertEquals(model_updated.updated_at, updated_at)
        self.assertEquals(model_updated.category.name, data['name'])

    def test_posters_delete(self):

        '''
        Delete post
        '''
        response = self.client.post(self.delete_post)
        self.assertTemplateUsed(response, 'posters/succesfully.html')
        self.assertEquals(response.context['message'], 'Post deleted succesfully')

#set_locator
# There would be the same class of Map, template