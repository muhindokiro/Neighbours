from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Majirani'
    sender = 'blaize1143@gmail.com'

    #passing the context vairables
    text_content = render_to_string('email/neighbourmail.txt',{"name": name})
    html_content = render_to_string('email/neighbourmail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()