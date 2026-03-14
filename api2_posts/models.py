from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title      =  models.CharField(max_length=20)
    content    =  models.TextField(max_length=500)
    img        =  models.ImageField(upload_to='posts/',null=True, blank=True)
    owner      =  models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def ___str__(self):
        return self.title 

