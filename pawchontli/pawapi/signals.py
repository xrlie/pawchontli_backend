import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def welcome_mail(sender, instance, created, **kwargs):
#   if created:
#     message = Mail(
#       from_email='paw.chontli@gmail.com',
#       to_emails='user01@vomoto.com',
#       subject='Welcome to Pawchontli',
#       html_content='<strong>We hope you and your new friend like each other</strong>')
#     try:
#         sg = SendGridAPIClient('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')
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e.message)