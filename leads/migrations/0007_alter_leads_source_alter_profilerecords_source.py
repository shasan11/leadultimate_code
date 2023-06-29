# Generated by Django 4.2.2 on 2023-06-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_remove_leads_email_text_leads_email_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='source',
            field=models.CharField(choices=[('IF', 'Instagram Followers'), ('IFG', 'Instagram Following'), ('WB', 'Website')], max_length=10, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='profilerecords',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Source (Social Media / Website)'),
        ),
    ]