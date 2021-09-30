from django import forms
from . models import NewsletterSubscribers, EmailMessage


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribers
        fields = ['email', ]


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = '__all__'
