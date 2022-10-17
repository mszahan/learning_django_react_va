from dataclasses import fields
from rest_framework import serializers
from blog.models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'slug', 'title', 'author', 'excerpt', 'content', 'status' )