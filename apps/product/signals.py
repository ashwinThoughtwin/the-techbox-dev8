from django.db.models.signals import post_save,post_init,post_delete
from django.db.models.signals import pre_save,pre_init,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Item
from django.core.mail import send_mail
from django.conf import settings
@receiver(post_save, sender=Item)
def create_item(sender, instance, created, **kwargs):
    if created:
        subject = 'Requesting for'
        message = 'Hi We providing you one gadgets'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["vivekram.techies123@gmail.com",]
        send_mail(subject, message, email_from, recipient_list)
        