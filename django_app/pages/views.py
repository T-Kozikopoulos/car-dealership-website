from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from dealers.models import Dealer


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    dealers = Dealer.objects.order_by('-hire_date')
    mvp_dealers = Dealer.objects.all().filter(is_mvp=True)

    context = {
        'dealers': dealers,
        'mvp_dealers': mvp_dealers,
    }

    return render(request, 'pages/about.html', context)
