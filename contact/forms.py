from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for Contact Model
    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

     
        # Sets placeholder on inputs
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Message Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'

        for field in self.fields:
            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'mb-3 px-2 py-2 rounded-0 shadow-sm text-black')