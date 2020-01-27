from django.db.models.signals import post_save
from django.dispatch import receiver

from client.models import Profile
from user.models import InstaUser


@receiver(post_save, sender=InstaUser, dispatch_uid='user_post_save')
def user_entry(sender, instance, **kwargs):
    if kwargs['created'] and instance.is_superuser is None and instance.is_staff:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
