from django.urls import path
from . import views
    

urlpatterns = [
    path('', views.list_post, name = 'list-post'),
    path('create/post', views.create_post, name='create-post'),
    path('edit/post/<int:pk>', views.edit_post, name='edit-post'),
    path('delete/post/<int:pk>', views.delete_post, name='delete-post'),
]