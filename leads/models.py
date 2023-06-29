from django.db import models
from tinymce.models import HTMLField 
 
SOCIAL_MEDIA = 'SM'
INSTA_FOLLOWERS = 'IF'
INSTA_FOLLOWING = 'IFG'
LINKEDIN_COMPANY = 'LC'
WEBSITE = 'WB'
    
SOURCE_CHOICES = [
         
        #(INSTA_FOLLOWERS, 'Instagram Followers'),
        (INSTA_FOLLOWING, 'Instagram Following'),
        (WEBSITE, 'Website'),
        
    ]
    
class Leads(models.Model):    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, verbose_name='Source')
    value = models.CharField(max_length=100, verbose_name='Values')
    
    class Meta:
        verbose_name_plural = 'Leads'
        verbose_name = 'Lead'
    
    def __str__(self):
        return self.name

class Task(models.Model):
    id=models.BigAutoField(primary_key=True)
    lead=models.ForeignKey(Leads,on_delete=models.CASCADE,verbose_name="Lead")
    name=models.CharField(max_length=100,verbose_name="Name")
    status=models.CharField(max_length=100,choices=(
        ("r","Running"),("c","Completed"),("s","Stopped")
    ),default="r")
    description=models.TextField(verbose_name="Description",null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Task Status'
        verbose_name = 'Task Status'
    
    def __str__(self):
        return self.name

class LeadsEmail(models.Model):
    id=models.BigAutoField(primary_key=True)
    lead=models.ForeignKey(Leads,on_delete=models.CASCADE,verbose_name="Lead",null=True,blank=True)
    email_subject = models.CharField(max_length=100, verbose_name='Email Subject',blank=True,null=True)
    email_body = HTMLField(blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Emails'
        verbose_name = 'Email'
    
    def __str__(self):
        return self.email_subject


 