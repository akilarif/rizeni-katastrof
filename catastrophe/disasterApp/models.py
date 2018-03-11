from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=32, null=True)
    location = models.CharField(max_length=32, null=True)
    birth_date = models.DateField(null=True)
    gender=models.CharField(max_length=8, null=True)
    email=models.EmailField(max_length=256, null=True)
    emergency_contact_name= models.CharField(max_length=32 ,null=True)
    emergency_email=models.EmailField(max_length=256 ,null=True)
    msg=models.CharField(max_length=256, null=True)
    emergency_no=models.CharField(max_length=64, null=True)
    contact_no=models.CharField(max_length=64, null=True)
    def __str__(self):
        return self.user
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Missing_Person(models.Model):
    Name = models.CharField(max_length=64)
    Age = models.CharField(max_length=4)
    Gender=models.TextField(max_length=16)
    Description=models.TextField(max_length=256)

    def publish(self):
        self.save()

    def __str__(self):
        return self.Name