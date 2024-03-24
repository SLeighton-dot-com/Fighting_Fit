from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, NewsletterSubscriber
from .forms import UserProfileForm, NewsletterForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import logging
from django.http import HttpResponseForbidden


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

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    
    # Check if the logged-in user is the one who made the order
    if order.email != request.user.email:
        # If not, show error message and redirect to profile page
        messages.error(request, "You don't have permission to view this order.")
        return redirect('profiles/profile.html')

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


logger = logging.getLogger(__name__)


def newsletter_subscribe(request):
    try:
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if NewsletterSubscriber.objects.filter(email=email).exists():
                    messages.error(request, 'This email address is already subscribed.')
                    redirect_path = request.POST.get('redirect_to', 'home')
                    return redirect(redirect_path)
                else:
                    form.save()
                    messages.success(request, 'Thank you for subscribing!')
                    redirect_path = request.POST.get('redirect_to', 'home')
                    return redirect(redirect_path)
            else:
                messages.error(request, 'Subscription failed. Please ensure the form is valid.')
                redirect_path = request.POST.get('redirect_to', 'home')
                return redirect(redirect_path)
        else:
            form = NewsletterForm()
            
        template = 'home/index.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
    except Exception as e:
        logger.exception("Failed to subscribe user to newsletter.")
        raise
