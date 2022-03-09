from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=255, null=False)
    profile_photo = models.ImageField(upload_to='images/', null=True, default='images/user_default_image.png')
    play = models.CharField(max_length=255, null=False, default='Boller')
    team =models.IntegerField(null=True, default=None)
    amount = models.PositiveBigIntegerField(default=None, null=True)
    
    def __str__(self):
        name = self.name
        return name

class team(models.Model):
    name = models.CharField(max_length=255, null=False)
    manager = models.CharField(max_length=255, null=False)
    owner = models.CharField(max_length=255, null=False)
    original_amount = models.PositiveBigIntegerField(default=None, null=True)
    balance_amount = models.PositiveBigIntegerField(default=None, null=True)

    def __str__(self):
        name = self.team_name
        return name