from email.policy import default
from django.db import models

# Create your models here.
class profile(models.Model):
    player_id = models.CharField(max_length=255, null=False, unique=True)
    profile_photo = models.ImageField(upload_to='images/', null=True, default='images/user_default_image.png')  
    team =models.CharField(max_length=255, null=True, default=None)
    amount = models.PositiveBigIntegerField(default=None, null=True)
    
    def __str__(self):
        name = self.player_id
        return name

class team(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    manager = models.CharField(max_length=255, null=False)
    owner = models.CharField(max_length=255, null=False)
    original_amount = models.PositiveBigIntegerField(default=None, null=True)
    balance_amount = models.PositiveBigIntegerField(default=None, null=True)

    def __str__(self):
        name = self.name
        return name

class auction_data(models.Model):
    player_id = models.CharField(max_length=255, null=False, unique=True)
    team = models.CharField(max_length=255, null=False, unique=True)
    amount = models.PositiveBigIntegerField(default=None, null=False)

    def __str__(self):
        name = self.player_id
        return name