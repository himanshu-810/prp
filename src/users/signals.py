from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

 #decorator

@receiver(post_save,sender=Profile)
def create_location_profile(sender,instance,created,**kwargs):
    if created:
        profile_location=Location.objects.create()
        instance.location=profile_location
        instance.save()
        #Location is defined in model and profile=instance due to onetoone mapping
@receiver(post_delete,sender=Profile)
def delete_location_profile(sender,instance,*args,**kwargs):
    if instance.location:
        instance.location.delete()