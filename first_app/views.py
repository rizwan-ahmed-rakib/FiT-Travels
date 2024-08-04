from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from first_app.models import (Settings, Nav_Links, HomeSlides, SideHomeSlides,
                              PresidentSpeach, AboutUs, TopManagement, Hazz_Message, HazzMustbeDone, Agency_Should,
                              Hazz_Tips, Image_Gallery, Video_Gallery, Notice, Form, Email_Inbox, Latest_news)


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
        context['president_speach'] = PresidentSpeach.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        context['latest_news'] = Latest_news.objects.all()
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
        context['about_us'] = AboutUs.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class ManagementPageView(TemplateView):
    template_name = 'about/topmanagement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['management'] = TopManagement.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class BaseView(TemplateView):
    template_name = 'travel/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
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
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context

class Speach(TemplateView):
    template_name = 'about/speach.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        # context['president_speach'] = PresidentSpeach.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        context['speach'] = PresidentSpeach.objects.get(pk=pk)
        return context


class HazzMessage(TemplateView):
    template_name = 'hazz-information/hazz_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['hazz_message'] = Hazz_Message.objects.all()
        context['notics'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class HazzMustBeDone(TemplateView):
    template_name = 'hazz-information/hazz_mustbe_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['hazz_mustbe_done'] = HazzMustbeDone.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class AgencyShould(TemplateView):
    template_name = 'hazz-information/agency-should.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['agency_should'] = Agency_Should.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class HazzTips(TemplateView):
    template_name = 'hazz-information/hazz-tips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['hazz_tips'] = Hazz_Tips.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class ImageGallery(TemplateView):
    template_name = 'galler/image_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        context['notices'] = Notice.objects.all()
        return context


class VideoGallery(TemplateView):
    template_name = 'galler/videoGallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['video_gallery'] = Video_Gallery.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class Notices(TemplateView):
    template_name = 'galler/notice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        # context['notice'] = Notice.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class NoticeDetail(TemplateView):
    template_name = 'galler/notice details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')  # Accessing the primary key
        context['pk'] = pk
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['notice'] = Notice.objects.get(pk=pk)
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class FormDownload(TemplateView):
    template_name = 'about/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['form'] = Form.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


class ContactUs(CreateView):
    template_name = 'about/contact.html'
    model = Email_Inbox
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()

        return context


class News_details(TemplateView):
    template_name = 'galler/newsDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        context['latest'] = Latest_news.objects.get(pk=pk)
        return context


class All_News(ListView):
    template_name = 'first_app/latest_news_list.html'
    model = Latest_news
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pk = self.kwargs.get('pk')
        context['sliders'] = HomeSlides.objects.all()
        context['side_sliders'] = SideHomeSlides.objects.all()
        context['settings'] = Settings.objects.all()
        context['notices'] = Notice.objects.all()
        context['image_gallery'] = Image_Gallery.objects.all()
        context['latest'] = Latest_news.objects.all
        return context


class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'login/adminsiteDashBoard.html'
