from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from posters.views import (
    list_post, 
    create_post, 
    edit_post, 
    delete_post, 
    show_post,
    set_geolocator,
    )
from posters.models import Post

class TestUrls(TestCase):

    '''
    The main objective of this test is assert if equal the resolve url with the reverse
    with primary keys
    '''

    def setUp(self):

        self.post = Post.objects.create(
            title = 'Example Title',
            description='lorem ipsum',
            content = 'lorem ipsum ipsum',
            status = 1,
            latitude = 10,
            longitude = 10,
        )
        self.pk = self.post.id

    def test_list_all_post_is_resolved(self):

        url = reverse('list-posters')
        self.assertEqual(resolve(url).func, list_post)
    

    def test_create_post_is_resolved(self):

        url = reverse('create-post')
        self.assertEqual(resolve(url).func, create_post)
    

    def test_edit_post_is_resolved(self):

        url = reverse('edit-post', kwargs={'pk': self.pk})
        self.assertEqual(resolve(url).func, edit_post)
    
    def test_delete_post_is_resolved(self):

        url = reverse('delete-post', kwargs={'pk': self.pk})
        self.assertEqual(resolve(url).func, delete_post)
    
    def test_show_post_is_resolved(self):

        url = reverse('show-post', kwargs={'pk': self.pk})
        self.assertEqual(resolve(url).func, show_post)

    def test_geocoder_is_resolved(self):

        #Both Working
        #url = reverse('geocoder', kwargs={'pk_post': 28})
        url = reverse('geocoder', args=[self.pk])
        self.assertEqual(resolve(url).func, set_geolocator)
 