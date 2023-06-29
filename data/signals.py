from data.models import SocialMediaCredentials
from django.db.models.signals import pre_migrate
from django.dispatch import receiver

@receiver(pre_migrate)
def create_first_record(sender, **kwargs):
    if sender.name == 'your_app':  # Replace 'your_app' with the name of your Django app
        if not SocialMediaCredentials.objects.exists():
            SocialMediaCredentials.objects.create()  # Create the first record with default values
