import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from celery import shared_task
from leads.models import Leads
from leads.profile import ProfileRecords

def get_emails_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    return emails

@shared_task
def scrape_emails_from_website(website_url, max_emails, lead_id):
    print("Web Scraping Function Accessed")
    domain = website_url.split('//')[1].split('/')[0]
    visited_urls = set()
    emails = set()
    urls_to_scrape = [website_url]

    while urls_to_scrape and len(emails) < max_emails:
        url = urls_to_scrape.pop(0)
        if url in visited_urls or not url.startswith('http'):
            continue
        visited_urls.add(url)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                current_emails = get_emails_from_url(url)
                for email in current_emails:
                    if domain in email and email not in emails:
                        emails.add(email)
                        instance = Leads.objects.get(pk=lead_id)
                        ProfileRecords.objects.create(leads=instance, email=email, source=website_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a'):
                    next_url = urljoin(url, link.get('href'))
                    urls_to_scrape.append(next_url)
                
        except (requests.exceptions.RequestException, AttributeError):
            pass

    return len(emails)
