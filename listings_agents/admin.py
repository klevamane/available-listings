from django.contrib import admin

from .models import Agent

# set up the model admin
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 10


# Register your models here.
admin.site.register(Agent, AgentAdmin)
