from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (IsAdminUser, 
                                        BasePermission, 
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        SAFE_METHODS)


#this class should be in a separate file named permissions.py
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user




class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer