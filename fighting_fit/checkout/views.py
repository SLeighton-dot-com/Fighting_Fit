from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OpF9kLlp1ZZh32ZBJh6kFBX0MeTviPiyLv4MtiEufPaiWnEUtdIDZop9019TD1nvJRpQ7wQIVCZ5TsCDG9KqzSA00xHhILQAj',
        'client_secret': 'sk_test_51OpF9kLlp1ZZh32Zi3L6lreJyYw7RPuC6gLHmf97IYA7GyfwZEctYTFt2DYZGJ6XPcGHsYqmSbh1CnJLRsdJ93ET00JsRJqrRK',
    }

    return render(request, template, context)