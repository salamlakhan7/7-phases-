from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SecurePost
from .serializers import SecurePostSerializers
import os

class SecurePostViewSet(ModelViewSet):
    queryset = SecurePost.objects.all()
    serializer_class = SecurePostSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SecurePost.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()

        # If new image uploaded, delete old image
        if 'image' in self.request.FILES:
            if instance.image:
                if os.path.isfile(instance.image.path):
                    os.remove(instance.image.path)

        serializer.save()

    def perform_destroy(self, instance):
        # Delete image from disk before deleting object
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
        instance.delete()