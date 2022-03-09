from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=255, null=False)
    profile_photo = models.ImageField(upload_to='images/', null=True, default='images/user_default_image.png')
    team =models.IntegerField(null=True, default=None)
    amount = models.PositiveBigIntegerField(default=None, null=True)

class team(models.Model):
    team_name = models.CharField(max_length=255, null=False)
    team_manager = models.CharField(max_length=255, null=False)
    team_owner = models.CharField(max_length=255, null=False)
    original_amount = models.PositiveBigIntegerField(default=None, null=True)
    balance_amount = models.PositiveBigIntegerField(default=None, null=True)