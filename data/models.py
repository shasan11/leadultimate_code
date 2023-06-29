from django.db import models
 
class SocialMediaCredentials(models.Model):
    pipedrive_api = models.CharField(max_length=100, default='default_pipedrive_api',verbose_name="Pipedrive Api")
    instagram_email = models.CharField(max_length=100, default='default_instagram_email',verbose_name="Instagram Email/Username")
    instagram_password = models.CharField(max_length=100, default='default_instagram_password',verbose_name="Instagram Password")
    linkedin_email = models.CharField(max_length=100, default='default_linkedin_email',verbose_name="Linkedin Email/Username")
    linkedin_password = models.CharField(max_length=100, default='default_linkedin_password',verbose_name="Password")

    def __str__(self):
        return("Social Media Credentials")
    class Meta:
        verbose_name = 'Social Media Credentials'
        verbose_name_plural = 'Social Media Credentials'

    def save(self, *args, **kwargs):
        # Ensure only one record is created by checking if the model already exists
        if not self.pk and SocialMediaCredentials.objects.exists():
            raise ValueError('Only one instance of MyModel can be created.')
        super().save(*args, **kwargs)
 