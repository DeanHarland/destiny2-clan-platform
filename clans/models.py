from django.db import models
from django.contrib.auth.models import User

class Clan(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)
    description = models.TextField()
    clan_type = models.CharField(max_length=50)

    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_clans')

    def __str__(self):
        return self.name
    
class ClanMembership(models.Model):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.clan.name}"