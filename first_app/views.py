from django.shortcuts import render
from django.views.generic import TemplateView
from first_app.models import Settings, Nav_Links, HomeSlides,SideHomeSlides,PresidentSpeach


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()

        # context['slider'] = HomeSlides
        # context['title'] = 'travel'
        return context


class AboutPageView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class ManagementPageView(TemplateView):
    template_name = 'about/topmanagement.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class BaseView(TemplateView):
    template_name = 'travel/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        return context


class HomePageTravellsView(TemplateView):
    template_name = 'travel/navBar.html'


class PresidenSpeach(TemplateView):
    template_name = 'about/presidentSpeach.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['president_speach'] = PresidentSpeach.objects.all()
        return context


class HazzMessage(TemplateView):
    template_name = 'hazz-information/hazz_message.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class HazzMustBeDone(TemplateView):
    template_name = 'hazz-information/hazz_mustbe_done.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class AgencyShould(TemplateView):
    template_name = 'hazz-information/agency-should.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class HazzTips(TemplateView):
    template_name = 'hazz-information/hazz-tips.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class ImageGallery(TemplateView):
    template_name = 'galler/image_gallery.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class VideoGallery(TemplateView):
    template_name = 'galler/videoGallery.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class Notices(TemplateView):
    template_name = 'galler/notice.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class FormDownload(TemplateView):
    template_name = 'about/form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class ContactUs(TemplateView):
    template_name = 'about/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        return context


class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'login/adminsiteDashBoard.html'


