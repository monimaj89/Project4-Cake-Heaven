from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.


def contact(request):
    # Handles Form Submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            subject = "Cake Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            # Join all of the body's values together, to format the email message.
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                return render(request, 'contact/success.html')
            # Return BadHeaderError to prevent attackers inserting extra email headers
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})