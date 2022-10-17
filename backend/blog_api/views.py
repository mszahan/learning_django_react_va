from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (IsAdminUser, 
                                        BasePermission,
                                        IsAuthenticated, 
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        SAFE_METHODS)


#this class should be in a separate file named permissions.py
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user




class PostList(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = PostSerializer
    queryset = Post.post_objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    #custom queryset
    def get_queryset(self):
        return Post.objects.all()





# class PostList(viewsets.ViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.post_objects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
    
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)



# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass



# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.post_objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.post_objects.all()
#     serializer_class = PostSerializer