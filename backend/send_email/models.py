from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
import smtplib


def send_email(email, message):
    from_email = 'faniamtest@gmail.com'
    password = 'sajjad20120'
    to_email = email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(from_email, password)
        massage = message
        server.sendmail(from_email, to_email, massage)
        server.quit()
        print("email sent")
    except:
        print("error")


def post_save_send_email(instance, created, *args, **kwargs):
    if created:
        user_email = instance.email
        subject = "subject: create"
        message = f"{subject}\nmessage: user created."
        send_email(user_email, message)


post_save.connect(post_save_send_email, sender=User)


def pre_delete_send_email(instance, *args, **kwargs):
    user_email = instance.email
    subject = "subject: delete"
    message = f"{subject}\nmessage: user delete."
    send_email(user_email, message)


pre_delete.connect(pre_delete_send_email, sender=User)
