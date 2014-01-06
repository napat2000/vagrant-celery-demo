from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'pub_date']

admin.site.register(Poll, PollAdmin)
