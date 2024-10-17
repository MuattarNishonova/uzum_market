from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Category


@receiver(post_save, sender=Category)
def send_welcome(sender, instance, created, **kwargs):
    print('Categoriya qo\'shildi ')
