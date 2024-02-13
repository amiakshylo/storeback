from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage

def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Andrew'}
        )
        message.send(['bob@gmail.com'])
    except BadHeaderError:
        pass
            
    return render(request, 'hello.html', {'name': 'Andrii'})
