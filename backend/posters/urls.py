from django.urls import path
from . import views
    

urlpatterns = [
    path('all/post', views.list_post, name = 'list-posters'),
    path('create/post', views.create_post, name='create-post'),
    path('edit/post/<int:pk>', views.edit_post, name='edit-post'),
    path('delete/post/<int:pk>', views.delete_post, name='delete-post'),
    path('show/post/<int:pk>', views.show_post, name='show-post'),
    #path('api/geocoder', views.geocoder, name='geocoder'),
    path('create/geolocator/<int:pk_post>', views.set_geolocator, name='geocoder'),
    path('thanks/', views.congratulation_post_created, name='thanks'),
]