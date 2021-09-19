from django import forms
from . models import NewsletterSubscribers, EmailMessage


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribers
        fields = ['email', ]
