from django import forms

from .models import Post

class Post(object):
    def __init__(self, *args):
        super(Post, self).__init__(*args))
        