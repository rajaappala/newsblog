# main/tasks.py
 
from django.core.mail import EmailMessage
from blog.celery import app
from django.conf import settings
 
 
@app.task
def notify_admin_via_email(message):
    email = EmailMessage('Notification!!!', message, to=[settings.ADMIN_EMAIL])
    email.send()
