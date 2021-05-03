import os
from os import getenv
from dotenv import load_dotenv
load_dotenv()

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

def check_related_object(user) :
  try:
    if user.adopters:
      return 'adopter'
  except:
    try:
      if user.associations:
        return 'association'
    except:
      return 'none'

@receiver(post_save, sender=User)
def welcome_mail(sender, instance, created, **kwargs):
  if created:
    # print(instance.username + ' was created!')
    if check_related_object(instance) == 'adopter':
      message = Mail(
        from_email='paw.chontli@gmail.com',
        to_emails=instance.email,
        subject='Welcome to Pawchontli',
        html_content=f'<strong>Welcome {instance.username}!<br> We are so excited to have you with us, and we hope you can find your missing friend soon.<br> Sincerely Pawchontli.</strong>')
    elif check_related_object(instance) == 'association':
      message = Mail(
        from_email='paw.chontli@gmail.com',
        to_emails=instance.email,
        subject='Welcome to Pawchontli',
        html_content=f'<strong>Welcome {instance.username}!<br> We are so excited to have you with us, and we hope your pets find a new family soon.<br> Sincerely Pawchontli.</strong>')  
    try:
      sg = SendGridAPIClient(getenv('SENDGRID_API_KEY'))
      response = sg.send(message)
      # print(response.status_code)
      # print(response.body)
      # print(response.headers)
    except Exception as e:
      print(e.message)

# post_save.connect(welcome_mail, sender=User)