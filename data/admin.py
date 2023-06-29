from django.contrib import admin
from .models import SocialMediaCredentials

class MyModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Pipedrive API', {
            'fields': ('pipedrive_api',),
        }),
        ('Instagram Credentials', {
            'fields': ('instagram_email', 'instagram_password'),
        }),
        ('LinkedIn Credentials', {
            'fields': ('linkedin_email', 'linkedin_password'),
        }),
    )

admin.site.register(SocialMediaCredentials, MyModelAdmin)
