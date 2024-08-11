from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from dashboard_app.forms import ImageGalleryForm, VideoGalleryForm
from first_app.models import (Image_Gallery, Video_Gallery, Notice, Settings, SideHomeSlides, HomeSlides,
                              PresidentSpeach, Latest_news, TopManagement, Hazz_Message, Hazz_Tips, Agency_Should,
                              AboutUs, HazzMustbeDone, Email_Inbox)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


# Create your views here.

class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'dashboard/index.html'


###################################################################Image Gallery#####################################
class ImageGallery(TemplateView):
    # template_name = 'dashboard/imagegallery.html'
    template_name = 'crud/image_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_gallery'] = Image_Gallery.objects.all()
        return context


# image gallery crud---------------------------------------------------------start

# View for the image gallery page
def image_gallery_view(request):
    image_gallery = Image_Gallery.objects.all()
    return render(request, 'crud/image_gallery.html', {'image_gallery': image_gallery})


# Create a new image
def image_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        Image_Gallery.objects.create(name=name, image=image)
    return redirect('dashBoard_app:image_gallery')


# Update image
def image_update_view(request):
    if request.method == 'POST':
        image_id = request.POST.get('id')
        image_instance = get_object_or_404(Image_Gallery, id=image_id)
        image_instance.name = request.POST.get('name')
        if 'image' in request.FILES:
            image_instance.image = request.FILES['image']
        image_instance.save()
    return redirect('dashBoard_app:image_gallery')


# Image detail for editing
def image_detail_view(request):
    image_id = request.GET.get('id')
    image_instance = get_object_or_404(Image_Gallery, id=image_id)
    data = {
        'id': image_instance.id,
        'name': image_instance.name,
        'image': image_instance.image.url
    }
    return JsonResponse(data)


# Delete image
def image_delete_view(request):
    image_id = request.GET.get('id')
    image_instance = get_object_or_404(Image_Gallery, id=image_id)
    image_instance.delete()
    return JsonResponse({'deleted': True})


# image gallery crud-----------------------------------------------------------End
#######################################################  Video Dallery    #################################################################


class videoGallery(TemplateView):
    template_name = 'dashboard/videoGallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_gallery'] = Video_Gallery.objects.all()
        return context

    # video gallery crud start -------------------------------------start


def video_create_view(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashBoard_app:videos')
    else:
        form = VideoGalleryForm()
    return render(request, 'dashboard/video_form.html', {'form': form})


def video_update_view(request, pk):
    video = get_object_or_404(Video_Gallery, pk=pk)
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('dashBoard_app:video_gallery')
    else:
        form = VideoGalleryForm(instance=video)
    return render(request, 'dashboard/video_form.html', {'form': form})


def video_delete_view(request, pk):
    video = get_object_or_404(Video_Gallery, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('dashBoard_app:videos')
    return render(request, 'dashboard/video_confirm_delete.html', {'video': video})


def video_detail_view(request, pk):
    video = get_object_or_404(Video_Gallery, pk=pk)
    return JsonResponse({
        'id': video.pk,
        'name': video.name,
        'video_url': video.video.url,
        'embed_url': video.add_video_from_any_link
    })


# video gallery crud end -------------------------------------end


####################################################################################################################################
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
