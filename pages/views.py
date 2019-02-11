from django.shortcuts import render
from django.http import HttpResponse

from listings_ad.models import Listing
from listings_agents.models import Agent
from listings_ad.search_choices import bedroom_choices, price_choices, state_choices
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
# Create your views here.


def index(request):
    # returns only 3 listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices

    }
    return render(request, 'pages/index.html', context)


def about(request):
    agents = Agent.objects.all().filter()
    agent_of_the_month = Agent.objects.all().filter(is_mvp=True)[0]# get the first, its like limit 1

    # try:
    #     agent_of_the_month = Agent.get.filter (is_mvp=True)[:1]
    # except ObjectDoesNotExist:
    context = {
        "agents": agents,
        "mvp": agent_of_the_month
    }
    return render(request, 'pages/about.html', context)

