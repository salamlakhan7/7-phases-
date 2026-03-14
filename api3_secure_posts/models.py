from django.db import models
from django.contrib.auth.models import User
import os

class SecurePost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    image = models.ImageField(
        upload_to='secure_posts/',
        null=True,
        blank=True
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete image file from storage when object deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title