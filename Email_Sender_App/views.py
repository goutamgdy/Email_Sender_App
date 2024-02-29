from django.shortcuts import render, redirect
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email_from = request.POST['email_from']
        recipient_list = [request.POST['recipient_list']]

        send_mail(subject, message, email_from, recipient_list)

        return redirect('success')

    return render(request, 'Email_Sender_App/send_email.html')