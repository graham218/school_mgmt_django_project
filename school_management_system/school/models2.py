from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from journal.settings import AUTH_USER_MODEL as User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_confirmed = models.BooleanField(default=False)
    reset_password = models.BooleanField(default=False)

    class Meta:
        app_label = 'auth'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()