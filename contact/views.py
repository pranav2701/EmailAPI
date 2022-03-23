from django.shortcuts import render
from django.core.mail import send_mail
from pathlib import Path


def index(request):
    return render(request, 'send/index.html')


def result(request):
    username = request.GET['username']
    mail = request.GET['mail_id']
    sender = 'abashedjester@gmail.com',
    recipient = [mail]
    image_path = 'contact/my_image.png'
    image_name = Path(image_path).name
    abs_path = 'https://images.vexels.com/media/users/3/246391/isolated/lists/73f72c0a6b0a9d4c1629b720e77a4dbe-western-welcome-sign.png'
    body_html = f"""
    <!doctype html>
        <html lang=en>
            <head>
                <meta charset=utf-8>
                <title>Hello {username} </title>
            </head>
            <body></br>
                <img src="{abs_path}" alt="Welcome Image"/>
            </body>
        </html>
    """

    send_mail('Hello ' + username,
              message="Hello",
              html_message=body_html,
              from_email='abashedjester@gmail.com',
              recipient_list=[mail],
              fail_silently=False)

    return render(request, 'send/index.html')
