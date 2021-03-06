from django.db import models

# Create your models here.


class NewsletterSubscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class EmailMessage(models.Model):
    EmailTitle = models.CharField(max_length=200, null=True)
    EmailBody = models.TextField(null=True)

    def __str__(self):
        return self.EmailTitle
