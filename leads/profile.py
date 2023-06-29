from django.db import models
from .models import Leads
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class ProfileRecords(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    leads = models.ForeignKey(Leads, on_delete=models.CASCADE, verbose_name='Lead')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    username = models.CharField(max_length=100, verbose_name='Username')
    source = models.CharField(max_length=100, blank=True, null=True, verbose_name='Source (Social Media / Website)')
    follower = models.IntegerField(blank=True, null=True, verbose_name='Follower')
    following = models.IntegerField(blank=True, null=True, verbose_name='Following')
    company = models.CharField(max_length=100, blank=True, null=True, verbose_name='Company')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')

    class Meta:
        verbose_name_plural = 'Profile Records'
        verbose_name = 'Profile Record'

    def __str__(self):
        return self.username
    
    

