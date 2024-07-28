from django.contrib import admin
from first_app.models import Settings, Nav_Links, HomeSlides, SideHomeSlides,PresidentSpeach

# Register your models here.
admin.site.register(Settings)
admin.site.register(Nav_Links)
admin.site.register(HomeSlides)
admin.site.register(SideHomeSlides)
admin.site.register(PresidentSpeach)