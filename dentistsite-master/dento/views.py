from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send mail
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from mail
            ['dev.yann12@gmail.com'],  # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})
