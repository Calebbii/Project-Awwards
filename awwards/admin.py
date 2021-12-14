from django.contrib import admin
from awwards.models import Profile, Project, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)