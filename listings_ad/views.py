from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Listing
from listings_ad.search_choices import price_choices, bedroom_choices, state_choices

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
    single_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": single_listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords) # check __icontains in the documentation

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms) #lte is "less than or equal to"

    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "listings": query_list,
        "values": request.GET # use this for preserving the search keywords in the front end eg. value= {{values.bathrom}}

    }
    return render(request, 'listings/search.html', context) # templates/listings/search.html