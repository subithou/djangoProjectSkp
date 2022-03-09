from django.db import models

# Create your models here.
class auction_admin(models.Model):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        name = self.username
        return name