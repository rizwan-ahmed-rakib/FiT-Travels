from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from dashboard_app.forms import ImageGalleryForm
from first_app.models import (Image_Gallery, Video_Gallery, Notice, Settings, SideHomeSlides, HomeSlides,
                              PresidentSpeach, Latest_news, TopManagement, Hazz_Message, Hazz_Tips, Agency_Should,
                              AboutUs, HazzMustbeDone, Email_Inbox)
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView


# Create your views here.

class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'dashboard/index.html'


class ImageGallery(TemplateView):
    template_name = 'crud/image_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_gallery'] = Image_Gallery.objects.all()
        return context

#image gallery crud---------------------------------------------------------start
class ImageGalleryCreateView(BSModalCreateView):
    template_name = 'crud/image gallery/image_gallery_create.html'
    form_class = ImageGalleryForm
    success_message = 'Success: Image was created.'
    success_url = reverse_lazy('dashboard:image_gallery')

class ImageGalleryUpdateView(BSModalUpdateView):
    model = Image_Gallery
    template_name = 'crud/image gallery/image_gallery_update.html'
    form_class = ImageGalleryForm
    success_message = 'Success: Image was updated.'
    success_url = reverse_lazy('dashBoard_app:image_gallery')

class ImageGalleryDeleteView(BSModalDeleteView):
    model = Image_Gallery
    template_name = 'crud/image gallery/image_gallery_delete.html'
    success_message = 'Success: Image was deleted.'
    success_url = reverse_lazy('dashBoard_app:image_gallery')
#image gallery crud-----------------------------------------------------------End


class videoGallery(TemplateView):
    template_name = 'dashboard/videoGallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_gallery'] = Video_Gallery.objects.all()
        return context


class HomeSlide(TemplateView):
    template_name = 'dashboard/homeslides.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['home_slides'] = HomeSlides.objects.all()
        return context


class SideSlide(TemplateView):
    template_name = 'dashboard/sideslide.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['side_slides'] = SideHomeSlides.objects.all()
        return context


class AddNotice(TemplateView):
    template_name = 'notice/addnotice.html'


class AllNotice(TemplateView):
    template_name = 'notice/allnotice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_notice'] = Notice.objects.all()
        return context


class AddAbout(TemplateView):
    template_name = 'notice/add_about.html'


class AllAbout(TemplateView):
    template_name = 'notice/all_about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_about'] = AboutUs.objects.all()
        return context


class AddNews(TemplateView):
    template_name = 'news/addnews.html'


class AllNews(TemplateView):
    template_name = 'news/allnews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_news'] = Latest_news.objects.all()
        return context


class AddSpeach(TemplateView):
    template_name = 'news/add_speach.html'


class AllSpeach(TemplateView):
    template_name = 'news/all_speach.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_speach'] = PresidentSpeach.objects.all()
        return context


class AddManagement(TemplateView):
    template_name = 'management/add_management.html'


class AllManagement(TemplateView):
    template_name = 'management/all_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_management'] = TopManagement.objects.all()
        return context


class FrontendMessage(TemplateView):
    template_name = 'news/frontend_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_inbox'] = Email_Inbox.objects.all()
        return context


class Settings(CreateView):
    template_name = 'management/settings.html'
    model = Settings
    fields = '__all__'

