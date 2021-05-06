import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Adopter, Association, AdoptionForm

"""Adopters Signal: Welcome email"""


@receiver(post_save, sender=Adopter)
def adopters_welcome_email(sender, instance, created, **kwargs):
    if created:
        message = Mail(
            from_email="paw.chontli@gmail.com",
            to_emails=instance.user.email,
            subject="Welcome to Pawchontli",
            html_content=f"<strong>Welcome {instance.user.username}!<br> We are so excited to have you with us, and we hope you can find your missing friend soon.<br> Sincerely Pawchontli.</strong>",
        )
        try:
            sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
            response = sg.send(message)
        except Exception as e:
            print(e)


"""Associations Signal: Welcome email"""


@receiver(post_save, sender=Association)
def associations_welcome_email(sender, instance, created, **kwargs):
    if created:
        message = Mail(
            from_email="paw.chontli@gmail.com",
            to_emails=instance.user.email,
            subject="Welcome to Pawchontli",
            html_content=f"<strong>Welcome {instance.user.username}!<br> We are so excited to have you with us, and we hope your pets find a new family soon.<br> Sincerely Pawchontli.</strong>",
        )
        try:
            sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
            response = sg.send(message)
        except Exception as e:
            print(e)


@receiver(post_save, sender=AdoptionForm)
def form_submission_notification(sender, instance, created, **kwargs):
    if created:
      adopters_message = Mail(
          from_email="paw.chontli@gmail.com",
          to_emails=instance.adopter.user.email,
          subject="Form Submission",
          html_content=f"<strong> Thank you {instance.adopter.user.username}! </strong> <br> Your form has been submitted.<br> The association will contact you as soon as they check your form.<br> Thank you for connecting with us.<br> Remember, Pawchontli is the bridge to your new friend.<br> Best regards.",
      )
      try:
          sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
          response = sg.send(adopters_message)
      except Exception as e:
          print(e)
      association_message = Mail(
          from_email="paw.chontli@gmail.com",
          to_emails=instance.pet.association.user.email,
          subject=f"A new form Submission for {instance.pet.name}",
          html_content=f"<strong> Dear {instance.pet.association.user.username}, </strong> <br> A new form has been submitted.<br> Please contact {instance.adopter.user.username} at {instance.adopter.user.email} to let him know his or her form is under review.<br> Thank you for connecting with us.<br> Remember, Pawchontli is the bridge that connects your pets with new families.<br> Best regards.",
      )
      try:
          sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
          response = sg.send(association_message)
      except Exception as e:
          print(e)


@receiver(pre_save, sender=AdoptionForm)
def notify_adopter_on_status_change(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        current = instance
        previous = AdoptionForm.objects.get(id=instance.id)
        if previous.status != current.status:
          content_body = 'nothing'
          if current.status == 'Approved':
            content_body = f"<strong> Dear {current.adopter.user.username}, </strong> <br> We are glad to inform you that your adoption form has been approved.<br> Please, contact {current.pet.association.user.username} at {current.pet.association.user.email} for more information.<br> Thank you for connecting with us.<br> Remember, Pawchontli is the bridge to your new friend.<br> Best regards."
          elif current.status == 'Rejected':
            content_body = f"<strong> Dear {current.adopter.user.username}, </strong> <br> We are sorry to inform you that your adoption form has been denied.<br> Please, contact {current.pet.association.user.username} at {current.pet.association.user.email} for more information.<br> Thank you for connecting with us.<br> Remember, Pawchontli is the bridge to your new friend.<br> Best regards."
          message = Mail(
              from_email="paw.chontli@gmail.com",
              to_emails=current.adopter.user.email,
              subject=f"Adoption form for {current.pet.name}",
              html_content= content_body,
          )
          try:
              sg = SendGridAPIClient(getenv("SENDGRID_API_KEY"))
              response = sg.send(message)
          except Exception as e:
              print(e)
