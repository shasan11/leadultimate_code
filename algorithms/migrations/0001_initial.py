# Generated by Django 4.2.2 on 2023-06-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_email', models.EmailField(max_length=254)),
                ('instagram_password', models.CharField(max_length=255)),
                ('pipedrive_api_key', models.CharField(max_length=255)),
                ('linkedin_email', models.EmailField(max_length=254)),
                ('linkedin_password', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Social Credentials',
            },
        ),
    ]
