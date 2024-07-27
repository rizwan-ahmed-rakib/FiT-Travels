from django.shortcuts import render
from django.views.generic import TemplateView
from first_app.models import Settings, Nav_Links, HomeSlides


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['email'] = Settings.email
        # context['mobile_number'] = Settings.mobile_number
        # context['company_name'] = Settings.company_name
        # context['slider_image'] = Settings.slider_image
        # context['logo_image'] = Settings.logoimage
        context['nav_links'] = Nav_Links.objects.all()
        context['settings'] = Settings.objects.all()
        context['slider_home_page'] = HomeSlides.objects.all()
        return context


class TravellsPageView(TemplateView):
    template_name = 'travel/index.html'


class AboutPageView(TemplateView):
    template_name = 'about/about.html'


class ManagementPageView(TemplateView):
    template_name = 'about/topmanagement.html'


class BaseView(TemplateView):
    template_name = 'travel/base.html'


class HomePageTravellsView(TemplateView):
    template_name = 'travel/navBar.html'


class PresidenSpeach(TemplateView):
    template_name = 'about/presidentSpeach.html'


class HazzMessage(TemplateView):
    template_name = 'hazz-information/hazz_message.html'


class HazzMustBeDone(TemplateView):
    template_name = 'hazz-information/hazz_mustbe_done.html'


class AgencyShould(TemplateView):
    template_name = 'hazz-information/agency-should.html'


class HazzTips(TemplateView):
    template_name = 'hazz-information/hazz-tips.html'


class ImageGallery(TemplateView):
    template_name = 'galler/image_gallery.html'


class VideoGallery(TemplateView):
    template_name = 'galler/videoGallery.html'


class Notices(TemplateView):
    template_name = 'galler/notice.html'


class FormDownload(TemplateView):
    template_name = 'about/form.html'

class ContactUs(TemplateView):
    template_name = 'about/contact.html'

class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):

    template_name = 'login/adminsiteDashBoard.html'