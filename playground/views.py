from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'user@gmail.com', ['bob@gmail.com'])
        message.attach_file('playground/static/images/dog.jpeg')
        message.send()
    except BadHeaderError:
        pass

    # try:
    #     mail_admins('subject', 'message')
    # except BadHeaderError:
    #     pass
        
    
    return render(request, 'hello.html', {'name': 'Andrii'})
