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
            #'category',
        ]
    
    '''
    def save(self, commit=True):

        instance = super().save(commit)
        instance.category = Category.objects.get_or_create(name = self.cleaned_data['name'])
        return instance
    '''    
class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment 
        fields = ['comment']