from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# from django.contrib.auth.models import Usercd

# Create your models here.


class Patient (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30, null=True)
    lastName = models.CharField(max_length=30, null=True)
    nationalCode = models.CharField(max_length=10, null=True)
    birthDay = models.DateField(null=True)
    gender = models.BinaryField(blank=False, editable=True, null=True)

    def __str__(self):
        return self.firstName

"""class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthDay = models.DateField(null=True)
    gender = models.BinaryField(blank=False, editable=True)
    phone_number=models.CharField(max_length=11)
    drugs_notes=models.TextField()
    diseases_notes=models.TextField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #instance.profile.save()
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)"""

class History(models.Model):
    patientId = models.ForeignKey("Patient",  on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    price = models.PositiveIntegerField()


class Visit(models.Model):
    #patientId = models.ForeignKey("Patient",  on_delete=models.CASCADE)
    name = models.CharField(max_length=30 , default='')
    phone_number = models.CharField(max_length=11 , default='')
    description = models.TextField(default='')
    time = models.DateTimeField(auto_now=False, auto_now_add=False)


class WorkTimes(models.Model):
    startTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    endTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    reserved = models.BooleanField(default=False , editable=True)

