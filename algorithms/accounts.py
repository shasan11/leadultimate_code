from django.db import models

class SocialCredentials(models.Model):
    instagram_email = models.EmailField()
    instagram_password = models.CharField(max_length=255)
    pipedrive_api_key = models.CharField(max_length=255)
    linkedin_email = models.EmailField()
    linkedin_password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Allow only one record in the database
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Prevent deletion of the record
        pass

    class Meta:
        verbose_name_plural = 'Social Credentials'
