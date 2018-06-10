# main/tasks.py
 
from django.core.mail import EmailMessage
from blog.celery import app
 
 
@app.task
def notify_admin_via_email(message):
    email = EmailMessage('Notification!!!', message, to=['rajashekarappala@gmail.com'])
    email.send()
