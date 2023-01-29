from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=Student)
def update_user_staff_flag(sender, instance, **kwargs):
    if instance.is_teacher:
        instance.user.is_staff = True
        instance.user.save()

    if not instance.is_teacher:
        instance.user.is_staff = False
        instance.user.save()
