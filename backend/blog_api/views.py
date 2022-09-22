import imp
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser



class PostList(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer