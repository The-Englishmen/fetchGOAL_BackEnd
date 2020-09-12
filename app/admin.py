from django.contrib import admin
from .models import League, Team, Federation, Tournament

# Register your models here.

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Federation)
admin.site.register(Tournament)