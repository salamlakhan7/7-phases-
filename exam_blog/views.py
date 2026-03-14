from django.shortcuts import render
import os 
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from exam_blog.permissions import IsOwnerOrReadOnly
from . models import Article
from . serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
   # permission_classes = [IsAuthenticated] # Only authenticated users can access the API
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Authenticated users can create, update, delete. Unauthenticated users can only read.
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        #return Article.objects.filter(owner=self.request.user) # only owner can see its articles , do actions on its articles
        return Article.objects.all() # all users can see all articles but only owner can do actions on its articles

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
    def perform_update(self, serializer):
        instance = self.get_object()

        # If new image uploaded, delete old image
        if 'cover_img' in self.request.FILES:
            if instance.cover_img:
                if os.path.isfile(instance.cover_img.path):
                    os.remove(instance.cover_img.path)

        serializer.save()

    def perform_destroy(self, instance):
        # Delete image from disk before deleting object
        if instance.cover_img:
            if os.path.isfile(instance.cover_img.path):
                os.remove(instance.cover_img.path)
        instance.delete()
    