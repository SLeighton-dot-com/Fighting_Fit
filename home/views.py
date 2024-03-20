from django.shortcuts import render
from checkout.models import Review

def index(request):
    """ A view to return the index page along with the reviews for the carousel """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)

def my_custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)
