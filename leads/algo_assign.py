from .models import Leads,Task,LeadsEmail
from algorithms.get_data import set_data
from algorithms.website_scraper import scrape_emails_from_website
from django.db.models.signals import post_save
from email_engine.send_mail import send_mail
from django.dispatch import receiver
@receiver(post_save, sender=Leads)
def call_insta_algo(sender, instance, created, **kwargs):
    print("Reciever Function Activated ")
    if instance.source == 'IFG':
        t=Task.objects.create(lead=instance,name="Task : "+instance.name,status="r")
        t.save()
        set_data.delay(lead_id=int(instance.id), username=str(instance.value),task_id=int(t.id))
        
    elif instance.source =="WB":
        t=Task.objects.create(lead=instance,name="Task"+instance.name,status="r")
        t.save()
        scrape_emails_from_website.delay(lead_id=int(instance.id),max_emails=50,website_url=str(instance.value))
    else:
        pass

@receiver(post_save, sender=LeadsEmail)
def call_insta_algo(sender, instance, created, **kwargs):
     send_mail.delay(lead_id=int(instance.lead.id),subject=instance.email_subject,message=instance.email_body)


     