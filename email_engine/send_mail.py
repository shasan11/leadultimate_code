from celery import shared_task
from leads.models import Leads
from leads.profile import ProfileRecords
from django.core.mail import send_mail

@shared_task
def sendmail(lead_id,subject,message):
    lead_instance=Leads.objects.get(id=lead_id)
    profile=ProfileRecords.objects.get(leads=lead_instance)
    emails=profile.email.all()
    for e in emails:
        send_mail(
            subject,
            message,
            "trail_email@cortifox.com",
            [e],
            fail_silently=False,)


    