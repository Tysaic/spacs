from unicodedata import category
from django import forms
from .models import (
    Category,
    Author,
    Post,
    Comment
)


class PostForm(forms.ModelForm):

    #category = forms.CharField(max_length=32)
    class Meta:

        model = Post 

        fields = [
            'title',
            'description',
            'content',
            'status',
            'address'
        ]

class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment 
        fields = ['comment']

class GeoLocatorForm(forms.Form):

    ubication = forms.CharField(label='ubication', max_length=128)
    longitude = forms.FloatField(max_value=15, min_value=1, required=False, widget=forms.HiddenInput())
    latitude = forms.FloatField(max_value=15, min_value=1, required=False, widget=forms.HiddenInput())
