from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . models import NewsletterSubscribers
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required

from . forms import SubscriberForm, NewsletterForm

# Create your views here.


def newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to our Newsletter!')
            return redirect('home')
    else:
        form = SubscriberForm
    context = {
        'form': form
    }
    return render(request, 'newsletter/subscribe.html', context)


@login_required
def send_newsletter(request):
    """ Send a Newsletter to the Newsletter subscriber email list """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    emails = NewsletterSubscribers.objects.all()
    data_frame = read_frame(emails, fieldnames=['email'])
    email_list = data_frame['email'].values.tolist()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('EmailTitle')
            message = form.cleaned_data.get('EmailBody')
            send_mail(
                title,
                message,
                '',
                email_list,
                fail_silently=False
            )
            messages.success(request, 'You have successfully sent a Newsletter to our subscribers!')
            return redirect('home')
    else:
        form = NewsletterForm
    context = {
        'form': form
    }
    return render(request, 'newsletter/send_newsletter.html', context)