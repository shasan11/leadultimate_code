# Generated by Django 4.2.2 on 2023-06-28 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_socialmediacredentials_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediacredentials',
            name='instagram_email',
            field=models.CharField(default='default_instagram_email', max_length=100, verbose_name='Instagram Email/Username'),
        ),
        migrations.AlterField(
            model_name='socialmediacredentials',
            name='linkedin_email',
            field=models.CharField(default='default_linkedin_email', max_length=100, verbose_name='Linkedin Email/Username'),
        ),
    ]