from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Listing


# Create your views here.


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    number_of_listings_per_page = 3
    paginator = Paginator(listings, number_of_listings_per_page)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }
    return render(request, 'listings/listings.html', context) # templates/listings/listings.html


# ensure to pass the id if passed in the urls.py
def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html') # templates/listings/search.html