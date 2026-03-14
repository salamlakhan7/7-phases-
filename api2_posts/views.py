from django.shortcuts import render
from .models import Post
from . serializers import PostSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)