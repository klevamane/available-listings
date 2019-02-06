from django.db import models
from datetime import datetime as dt
from listings_agents.models import Agent

# Create your models here.


class Listing(models.Model):

    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING) # when an agent is deleted, the listing stays unaffected
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # the location inside the media folder that the image will be stored
    secondary_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    secondary_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    secondary_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    secondary_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    secondary_photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    secondary_photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # the location inside the media folder that the image will be stored
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=dt.now, blank=True)

    def __self__(self):
        return self.title
