from django.contrib import admin
from .models import NewsletterSubscribers, EmailMessage

# Register your models here.

admin.site.register(NewsletterSubscribers)
admin.site.register(EmailMessage)
