from django.contrib import admin

# Register your models here.

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """This class customizes what is being displayed in the admin section"""

    # list what is to be displayed in the admin section under the Model listings
    list_display = ('id', 'title', 'is_published')
    # headings that will be click-able as links
    list_display_links = ('id', 'title')
    # implement filter by
    list_filter = ('agent',)

    list_editable = ('is_published',)
    # number of max items to be displayed per page
    list_per_page = 5
    search_fields = ('title', 'price', 'city', 'state')

# remember to add the class here
admin.site.register(Listing, ListingAdmin)
