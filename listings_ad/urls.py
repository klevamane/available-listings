from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listings'),

    # listings_ad/23
    path('<int:listing_id>', views.listing, name='listing'),
    # listing_ad/search
    path('search', views.search, name='search')
]
