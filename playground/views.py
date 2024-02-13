from django.shortcuts import render
from django.core.mail import mail_admins, send_mail, BadHeaderError


def say_hello(request):
    try:
        send_mail('subject', 'message', 'user@gmail.com', ['bob@gmail.com'], html_message='message')
    except BadHeaderError:
        pass

    try:
        mail_admins('subject', 'message')
    except BadHeaderError:
        pass
        
    
    return render(request, 'hello.html', {'name': 'Andrii'})
