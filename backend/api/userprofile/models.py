from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    district = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_image')
    def __str__(self):
        return self.user.username