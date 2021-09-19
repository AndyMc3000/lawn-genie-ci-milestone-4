from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import SubscriberForm

# Create your views here.


def newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            return redirect('home')
    else:
        form = SubscriberForm
    context = {
        'form': form
    }
    return render(request, 'newsletter/subscribe.html', context)
