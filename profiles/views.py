from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, NewsletterForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def newsletter_subscribe(request):
    print("Request Path:", request.path)  # Debugging line
    if request.method == 'POST':
        print("Form Data:", request.POST)  # Debugging line
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            redirect_path = request.POST.get('redirect_to', '/')
            return redirect(redirect_path)
        else:
            messages.error(
                request, 'Subscription failed. Please ensure the form is valid.')
    else:
        form = NewsletterForm()
        
    template = 'home/index.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
