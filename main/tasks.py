from django.core.mail import send_mail

from main.celery import app
from main.models import Contact
from main.service import send


@app.task
def send_spam_email(email):
    send(email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
        'вы подписались на рассылку',
        'будет много спама',
        'leatheberner@gmail.com',
        [email],
        fail_silently=False,
    )