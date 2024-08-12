from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView

from dashboard_app.forms import ImageGalleryForm, VideoGalleryForm, NoticeForm
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
    template_name = 'dashboard/videogallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_gallery'] = Video_Gallery.objects.all()
        return context


# Create a new video
def video_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        video = request.FILES.get('video')
        add_video_from_any_link = request.POST.get('add_video_from_any_link')
        # thumbnail = request.FILES.get('thumbnail')
        Video_Gallery.objects.create(name=name, video=video,
                                     add_video_from_any_link=add_video_from_any_link)  # thumbnail=thumbnail
    return redirect('dashBoard_app:videos')


def video_update_view(request):
    if request.method == 'POST':
        video_id = request.POST.get('id')
        video_instance = get_object_or_404(Video_Gallery, id=video_id)

        # Update the name
        video_instance.name = request.POST.get('name')

        # Update video file if provided, otherwise keep the existing one
        if 'video' in request.FILES:
            video_instance.video = request.FILES['video']

        # Update thumbnail if provided, otherwise keep the existing one
        if 'thumbnail' in request.FILES:
            video_instance.thumbnail = request.FILES['thumbnail']

        # Update video link, handle cases where it might be empty
        video_link = request.POST.get('add_video_from_any_link')
        if video_link:
            video_instance.add_video_from_any_link = video_link

        video_instance.save()

    return redirect('dashBoard_app:videos')


# Video detail for editing
def video_detail_view(request):
    video_id = request.GET.get('id')
    video_instance = get_object_or_404(Video_Gallery, id=video_id)
    data = {
        'id': video_instance.id,
        'name': video_instance.name,
        'video': video_instance.video.url if video_instance.video else '',
        'add_video_from_any_link': video_instance.add_video_from_any_link,
        'thumbnail': video_instance.thumbnail.url if video_instance.thumbnail else '',
    }
    return JsonResponse(data)


# Delete video
def video_delete_view(request):
    video_id = request.GET.get('id')
    video_instance = get_object_or_404(Video_Gallery, id=video_id)
    video_instance.delete()
    return JsonResponse({'deleted': True})


# video gallery crud end -------------------------------------end

################################################### home Sliders#################################################################################
class HomeSlide(TemplateView):
    template_name = 'dashboard/homeslides.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['home_slides'] = HomeSlides.objects.all()
        return context

    # crud start ------------------------------------------------start


class CreateHomeSlide(View):
    def post(self, request):
        title = request.POST.get('title', None)
        slide_picture = request.FILES.get('slide_picture', None)

        if title and slide_picture:
            new_slide = HomeSlides.objects.create(title=title, slide_picture=slide_picture)
            slide = {
                'id': new_slide.id,
                'title': new_slide.title,
                'slide_picture': new_slide.slide_picture.url,
            }
            # return JsonResponse({'slide': slide})

        # return JsonResponse({'error': 'Invalid data'}, status=400)

        return redirect('dashBoard_app:home_slides')


class UpdateHomeSlide(View):
    def post(self, request):
        slide_id = request.POST.get('id', None)
        title = request.POST.get('title', None)
        slide_picture = request.FILES.get('slide_picture', None)

        slide = get_object_or_404(HomeSlides, id=slide_id)
        if title:
            slide.title = title
        if slide_picture:
            slide.slide_picture = slide_picture
        slide.save()

        updated_slide = {
            'id': slide.id,
            'title': slide.title,
            'slide_picture': slide.slide_picture.url,
        }
        # return JsonResponse({'slide': updated_slide})

        return redirect('dashBoard_app:home_slides')


class DeleteHomeSlide(View):
    def post(self, request):
        slide_id = request.POST.get('id', None)
        slide = get_object_or_404(HomeSlides, id=slide_id)
        slide.delete()
        return JsonResponse({'deleted': True})


# crud end ------------------------------------------------end


###############################################   Side Sliders ##########################################################################
class SideSlide(TemplateView):
    template_name = 'dashboard/sideslide.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['side_slides'] = SideHomeSlides.objects.all()
        return context


# Create a new side slide
def side_slide_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        side_slide_picture = request.FILES.get('side_slide_picture')
        SideHomeSlides.objects.create(title=title, side_slide_picture=side_slide_picture)
    return redirect('dashBoard_app:side_slides')


# Update an existing side slide
def side_slide_update_view(request):
    if request.method == 'POST':
        slide_id = request.POST.get('id')
        slide_instance = get_object_or_404(SideHomeSlides, id=slide_id)
        slide_instance.title = request.POST.get('title')
        if 'side_slide_picture' in request.FILES:
            slide_instance.side_slide_picture = request.FILES['side_slide_picture']
        slide_instance.save()
    return redirect('dashBoard_app:side_slides')


# Get side slide details for editing
def side_slide_detail_view(request):
    slide_id = request.GET.get('id')
    slide_instance = get_object_or_404(SideHomeSlides, id=slide_id)
    data = {
        'id': slide_instance.id,
        'title': slide_instance.title,
        'side_slide_picture': slide_instance.side_slide_picture.url
    }
    return JsonResponse(data)


# Delete a side slide
def side_slide_delete_view(request):
    slide_id = request.GET.get('id')
    slide_instance = get_object_or_404(SideHomeSlides, id=slide_id)
    slide_instance.delete()
    return JsonResponse({'deleted': True})


#########################################################################################################################
class AddNotice(TemplateView):
    template_name = 'notice/addnotice.html'


class AllNotice(TemplateView):
    template_name = 'notice/allnotice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_notice'] = Notice.objects.all()
        return context


def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashBoard_app:notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notice/allnotice.html', {'form': form, 'action': 'Create'})


# Update a notice
def notice_update(request):
    notice_id = request.POST.get('id') if request.method == 'POST' else request.GET.get('id')
    notice_instance = get_object_or_404(Notice, id=notice_id)

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response indicating success
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # Return form errors in JSON
    else:
        form = NoticeForm(instance=notice_instance)
        return JsonResponse({
            'id': notice_instance.id,
            'subject': notice_instance.subject,
            'notice_body': notice_instance.notice_body,
            'file': notice_instance.file.url if notice_instance.file else None,
        })


# Get details of a notice for editing
def notice_detail(request):
    notice_id = request.GET.get('id')
    notice_instance = get_object_or_404(Notice, id=notice_id)
    data = {
        'id': notice_instance.id,
        'subject': notice_instance.subject,
        'notice_body': notice_instance.notice_body,
        'file': notice_instance.file.url if notice_instance.file else None,
    }
    return JsonResponse(data)


# Delete a notice
def notice_delete(request):
    notice_id = request.GET.get('id')
    notice_instance = get_object_or_404(Notice, id=notice_id)
    notice_instance.delete()
    return JsonResponse({'deleted': True})


#######################################################################################################################
class AddAbout(TemplateView):
    template_name = 'notice/add_about.html'


class AllAbout(TemplateView):
    template_name = 'notice/all_about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_about'] = AboutUs.objects.all()
        return context


class EditAbout(UpdateView):
    template_name = 'notice/edit_about.html'
    model = AboutUs
    fields = ('image', 'name', 'about_us')
    success_url = reverse_lazy('dashBoard_app:all_about')


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
