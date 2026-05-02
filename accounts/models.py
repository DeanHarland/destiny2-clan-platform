from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    bungie_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username
    
    #Auto-create Profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()