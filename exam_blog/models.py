from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=15)
    body = models.TextField(max_length=500)
    cover_img = models.ImageField(upload_to='exam_articles/', null=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
            # Delete image file from storage when object deleted
        if self.cover_img:
            if os.path.isfile(self.cover_img.path):
                os.remove(self.cover_img.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    
    # def __str__(self):
    #     return self.title