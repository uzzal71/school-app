from django.db import models
from profiles.models import UserProfile

class Teacher(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    mobile = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
