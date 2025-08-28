from django.contrib import admin
from django.utils.html import format_html
from first_app.models import (Settings, Nav_Links, HomeSlides, SideHomeSlides, PresidentSpeach,
                              AboutUs, TopManagement, Hazz_Message, HazzMustbeDone, Agency_Should, Hazz_Tips,
                              Image_Gallery, Video_Gallery,Notice,Form,Email_Inbox,Latest_news)
from embed_video.admin import AdminVideoMixin


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Settings)
admin.site.register(Nav_Links)
admin.site.register(HomeSlides)
admin.site.register(SideHomeSlides)
admin.site.register(PresidentSpeach)
admin.site.register(AboutUs)
admin.site.register(TopManagement)
admin.site.register(Hazz_Message)
admin.site.register(HazzMustbeDone)
admin.site.register(Agency_Should)
admin.site.register(Hazz_Tips)
admin.site.register(Image_Gallery)
admin.site.register(Video_Gallery,AdminVideo)
admin.site.register(Notice)
admin.site.register(Form)
admin.site.register(Email_Inbox)
admin.site.register(Latest_news)
