from django.contrib import admin
from carddecks.models import *

# Register your models here.
admin.site.register(Deck)
admin.site.register(Card)