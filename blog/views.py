from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Post
from blog.serializers import PostSerializers



class PostListCreateAPIView(ListCreateAPIView):
    """
        API view to retrieve list of posts or create new

    """
    serializer_class = PostSerializers
    queryset = Post.objects.all()

class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()