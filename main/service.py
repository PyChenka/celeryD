from django.core.mail import send_mail


def send(email):
    send_mail(
        'вы подписались на рассылку',
        'будет много спама',
        'leatheberner@gmail.com',
        [email],
        fail_silently=False,
    )
