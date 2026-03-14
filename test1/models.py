from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Test (models.Model):
    owner            = models.ForeignKey(User, on_delete=models.CASCADE)
    test_score       = models.IntegerField(default=0)
    rank             = models.CharField(max_length=15)
    is_medical_clear = models.BooleanField(default=False)
    
    def __str__(self):
        return self.rank
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token_version = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username   
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)