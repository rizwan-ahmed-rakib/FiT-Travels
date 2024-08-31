from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView, ListView

from dashboard_app.forms import ImageGalleryForm, VideoGalleryForm, NoticeForm  # AboutUsForm
from first_app.models import (Image_Gallery, Video_Gallery, Notice, Settings, SideHomeSlides, HomeSlides,
                              PresidentSpeach, Latest_news, TopManagement, Hazz_Message, Hazz_Tips, Agency_Should,
                              AboutUs, Form, HazzMustbeDone, Email_Inbox)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from first_app.views import Speach
from registration_app.models import Profile


# Create your views here.

def inbox_view(request):
    unseen_messages = Email_Inbox.objects.filter(seen=False).order_by('-date')
    message_count = unseen_messages.count()
    return render(request, 'notification.html', {'unseen_messages': unseen_messages, 'message_count': message_count})


class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unseen_messages'] = Email_Inbox.objects.filter(seen=False).order_by('-date')
        context['message_count'] = Email_Inbox.objects.filter(seen=False).order_by('-date').count()
        return context


###################################################################Image Gallery#####################################
class ImageGallery(TemplateView):
    # template_name = 'dashboard/imagegallery.html'
    template_name = 'crud/image_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_gallery'] = Image_Gallery.objects.all()
        context['profile'] = Profile.objects.all()
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
        video_link = request.POST.get('add_video_from_any_link')
        # video_file = request.FILES.get('video')
        # thumbnail = request.FILES.get('thumbnail')

        Video_Gallery.objects.create(
            name=name,
            add_video_from_any_link=video_link,
            # video=video_file,
            # thumbnail=thumbnail
        )

    return redirect('dashBoard_app:videos')


def video_update_view(request):
    if request.method == 'POST':
        video_id = request.POST.get('id')
        video_instance = get_object_or_404(Video_Gallery, id=video_id)

        # Update the name and video link
        video_instance.name = request.POST.get('name')
        video_link = request.POST.get('add_video_from_any_link')
        if video_link:
            video_instance.add_video_from_any_link = video_link

        # video_file = request.FILES.get('video')
        # if video_file:
        #     video_instance.video = video_file

        video_instance.save()

    return redirect('dashBoard_app:videos')


def video_detail_view(request):
    video_id = request.GET.get('id')
    video_instance = get_object_or_404(Video_Gallery, id=video_id)
    data = {
        'id': video_instance.id,
        'name': video_instance.name,
        'add_video_from_any_link': video_instance.add_video_from_any_link,
    }
    return JsonResponse(data)


def video_delete_view(request):
    if request.method == 'POST':
        video_id = request.POST.get('id')
        video_instance = get_object_or_404(Video_Gallery, id=video_id)
        video_instance.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'deleted': False})


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


# class UpdateHomeSlide(View):
#     def post(self, request):
#         slide_id = request.POST.get('id', None)
#         title = request.POST.get('title', None)
#         slide_picture = request.FILES.get('slide_picture', None)
#
#         slide = get_object_or_404(HomeSlides, id=slide_id)
#         if title:
#             slide.title = title
#         if slide_picture:
#             slide.slide_picture = slide_picture
#         slide.save()
#
#         updated_slide = {
#             'id': slide.id,
#             'title': slide.title,
#             'slide_picture': slide.slide_picture.url,
#         }
#
#         # return JsonResponse({'slide': updated_slide})
#         return redirect('dashBoard_app:home_slides')
# class UpdateHomeSlide(View):
#     def post(self, request):
#         slide_id = request.POST.get('id', None)
#         if not slide_id:
#             return JsonResponse({'error': 'Slide ID is missing.'}, status=400)
#
#         title = request.POST.get('title', None)
#         slide_picture = request.FILES.get('slide_picture', None)
#
#         slide = get_object_or_404(HomeSlides, id=slide_id)
#         if title:
#             slide.title = title
#         if slide_picture:
#             slide.slide_picture = slide_picture
#         slide.save()
#
#         updated_slide = {
#             'id': slide.id,
#             'title': slide.title,
#             'slide_picture': slide.slide_picture.url,
#         }
#
#         return redirect('dashBoard_app:home_slides')
def home_slide_update_view(request):
    if request.method == 'POST':
        image_id = request.POST.get('id')
        image_instance = get_object_or_404(HomeSlides, id=image_id)
        image_instance.name = request.POST.get('title')
        if 'slide_picture' in request.FILES:
            image_instance.slide_picture = request.FILES['slide_picture']
        image_instance.save()
    return redirect('dashBoard_app:home_slides')


def home_slide_detail_view(request):
    image_id = request.GET.get('id')
    image_instance = get_object_or_404(HomeSlides, id=image_id)
    data = {
        'id': image_instance.id,
        'name': image_instance.title,
        'image': image_instance.slide_picture.url
    }
    return JsonResponse(data)


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
class AddNotice(CreateView):
    template_name = 'notice/addnotice.html'
    model = Notice
    fields = ('file', 'subject', 'notice_body')
    success_url = reverse_lazy('dashBoard_app:all_notice')
    context_object_name = 'notice'


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
class AddAbout(CreateView):
    template_name = 'notice/add_about.html'
    model = AboutUs
    fields = ('image', 'name', 'about_us')
    # form_class = AboutUsForm
    success_url = reverse_lazy('dashBoard_app:all_about')


class AllAbout_delete(DeleteView):
    template_name = 'notice/delete_about.html'
    model = AboutUs
    success_url = reverse_lazy('dashBoard_app:all_about')
    context_object_name = 'all_about_delete'


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['about'] = AboutUs.objects.get(pk=pk)

        return context


#############################################################################################################################
class AddNews(CreateView):
    template_name = 'news/addnews.html'
    model = Latest_news
    fields = ('picture', 'headline', 'news_details')
    success_url = reverse_lazy('dashBoard_app:all_news')


class AllNews(TemplateView):
    template_name = 'news/allnews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_news'] = Latest_news.objects.all()
        return context


class EditNews(UpdateView):
    template_name = 'news/editnews.html'
    model = Latest_news
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['all_news'] = Latest_news.objects.get(pk=pk)
        return context


class DeleteNews(DeleteView):
    template_name = 'news/delete_news.html'
    model = Latest_news
    success_url = reverse_lazy('dashBoard_app:all_news')
    context_object_name = 'all_news'


class News_detail(DetailView):
    template_name = 'news/detail_news.html'
    model = Latest_news
    context_object_name = 'all_news'


######################################################################################################
class AddSpeach(CreateView):
    template_name = 'news/add_speach.html'
    model = PresidentSpeach
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_speach')


class AllSpeach(TemplateView):
    template_name = 'news/all_speach.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['all_speach'] = PresidentSpeach.objects.all()
        return context


class EditSpeach(UpdateView):
    template_name = 'news/update_speach.html'
    model = PresidentSpeach
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_speach')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['all_speach'] = PresidentSpeach.objects.get(pk=pk)
        return context


class DeleteSpeach(DeleteView):
    template_name = 'news/delete_speach.html'
    model = PresidentSpeach
    success_url = reverse_lazy('dashBoard_app:all_speach')
    context_object_name = 'all_speach'


class Speach_detail(DetailView):
    template_name = 'news/details_speach.html'
    model = PresidentSpeach
    context_object_name = 'all_speach'


#################################################################################
class AddManagement(CreateView):
    template_name = 'management/add_management.html'
    model = TopManagement
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_management')


class AllManagement(TemplateView):
    template_name = 'management/all_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['top_management'] = TopManagement.objects.all()
        return context


class EditMaagement(UpdateView):
    template_name = 'management/update_management.html'
    model = TopManagement
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_management')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['management'] = TopManagement.objects.get(pk=pk)
        return context


class DeleteMaagement(DeleteView):
    template_name = 'management/delete_management.html'
    model = TopManagement
    success_url = reverse_lazy('dashBoard_app:all_management')
    context_object_name = 'all_management'


class Maagement_detail(DetailView):
    template_name = 'management/details_management.html'
    model = TopManagement
    context_object_name = 'all_management'


#############################hazz message###########################################################
class AllHazzMessage(TemplateView):
    template_name = 'service/hazzmessage/all_hazz_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['haze_m'] = Hazz_Message.objects.all()
        return context


class EditHazzMessage(UpdateView):
    template_name = 'service/edit_service.html'
    model = Hazz_Message
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_message')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['haze_m'] = Hazz_Message.objects.get(pk=pk)
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_message')
        context['heading'] = "Hazz Message"
        return context


class DeleteHazzMessage(DeleteView):
    template_name = 'service/delete_service.html'
    model = Hazz_Message
    success_url = reverse_lazy('dashBoard_app:all_hazz_message')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_message')
        context['heading'] = "Hazz Message"
        return context


class HazzMessage_detail(DetailView):
    template_name = 'service/details.html'
    model = Hazz_Message
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_message')
        context['heading'] = "Hazz Message"
        return context


class AddHazzMessage(CreateView):
    template_name = 'service/add_service.html'
    model = Hazz_Message
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_message')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_message')
        context['heading'] = "Hazz Message"
        return context

    ##############################hazz must be done##########################################################


class AllHazzMustbeDone(TemplateView):
    template_name = 'service/hazzmustbedone/all_hazz_must_be_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['haze_m'] = HazzMustbeDone.objects.all()
        return context


class EditHazzMustbeDone(UpdateView):
    template_name = 'service/edit_service.html'
    model = HazzMustbeDone
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')
        context['heading'] = "Hazz Mustbe Done"
        context['haze_m'] = HazzMustbeDone.objects.get(pk=pk)
        return context


class DeleteHazzMustbeDone(DeleteView):
    template_name = 'service/delete_service.html'
    model = HazzMustbeDone
    success_url = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')
        context['heading'] = "Hazz Mustbe Done"
        return context


class HazzMustbeDone_detail(DetailView):
    template_name = 'service/details.html'
    model = HazzMustbeDone
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')
        context['heading'] = "Hazz Mustbe Done"
        return context


class AddHazzMustbeDone(CreateView):
    template_name = 'service/add_service.html'
    model = HazzMustbeDone
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_mustbe_done')
        context['heading'] = "Hazz Mustbe Done"
        return context


##############################agency should##########################################################
class AllAgencyShould(TemplateView):
    template_name = 'service/agencyshould/all_agency_should.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['haze_m'] = Agency_Should.objects.all()
        return context


class EditAgencyShould(UpdateView):
    template_name = 'service/edit_service.html'
    model = Agency_Should
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_agency_should')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['custom_url'] = reverse_lazy('dashBoard_app:all_agency_should')
        context['heading'] = "Agency Should"
        context['haze_m'] = Agency_Should.objects.get(pk=pk)
        return context


class DeleteAgencyShould(DeleteView):
    template_name = 'service/delete_service.html'
    model = Agency_Should
    success_url = reverse_lazy('dashBoard_app:all_agency_should')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_agency_should')
        context['heading'] = "Agency Should"
        return context


class AgencyShould_detail(DetailView):
    template_name = 'service/details.html'
    model = Agency_Should
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_agency_should')
        context['heading'] = "Agency Should"
        return context


class AddAgencyShould(CreateView):
    template_name = 'service/add_service.html'
    model = Agency_Should
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_agency_should')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_agency_should')
        context['heading'] = "Agency Should"
        return context


##############################hazz tips##########################################################
class AllHazzTips(TemplateView):
    template_name = 'service/hazztips/all_hazz_tips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['haze_m'] = Hazz_Tips.objects.all()
        return context


class EditHazzTips(UpdateView):
    template_name = 'service/edit_service.html'
    model = Hazz_Tips
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_tips')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_tips')
        context['heading'] = "Hazz Tips"
        context['haze_m'] = Hazz_Tips.objects.get(pk=pk)
        return context


class DeleteHazzTips(DeleteView):
    template_name = 'service/delete_service.html'
    model = Hazz_Tips
    success_url = reverse_lazy('dashBoard_app:all_hazz_tips')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_tips')
        context['heading'] = "Hazz Tips"
        return context


class HazzTips_detail(DetailView):
    template_name = 'service/details.html'
    model = Hazz_Tips
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_tips')
        context['heading'] = "Hazz Tips"
        return context


class AddHazzHazzTips(CreateView):
    template_name = 'service/add_service.html'
    model = Hazz_Tips
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_hazz_tips')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_tips')
        context['heading'] = "Hazz Tips"
        return context


########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
class FrontendMessage(TemplateView):
    template_name = 'news/frontend_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_inbox'] = Email_Inbox.objects.all().order_by('seen', '-date')

        return context


# class FrontendMessage(TemplateView):
#     template_name = 'news/frontend_message.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Retrieve the search parameters from the POST request
#         sl_number = self.request.POST.get('sl_number')
#         message_type = self.request.POST.get('type')
#         date_from = self.request.POST.get('dateFrom')
#         date_to = self.request.POST.get('dateTo')
#
#         # Get all email inbox messages
#         email_inbox = Email_Inbox.objects.all()
#
#         # Filter based on SL number if provided
#         if sl_number:
#             # SL number is the position in the queryset, so filter by index
#             try:
#                 sl_number = int(sl_number)
#                 email_inbox = email_inbox[sl_number - 1:sl_number]  # Convert SL number to 0-based index
#             except (ValueError, IndexError):
#                 email_inbox = Email_Inbox.objects.none()  # Return an empty queryset if invalid SL number
#
#         # Filter by message type if provided
#         if message_type:
#             email_inbox = email_inbox.filter(type=message_type)
#
#         # Filter by date range if provided
#         if date_from and date_to:
#             email_inbox = email_inbox.filter(date__range=[date_from, date_to])
#
#         context['email_inbox'] = email_inbox
#         return context


class FrontendMessageSearchView(TemplateView):
    template_name = 'news/frontend_message.html'  # Adjust the template name if necessary

    def post(self, request, *args, **kwargs):
        # Retrieve form data from POST request
        date_from = request.POST.get('dateFrom') #<input type="text" name="dateFrom" class="form-control datepicker" placeholder="Date from">
        date_to = request.POST.get('dateTo')  #<input type="text" name="dateTo" class="form-control datepicker" placeholder="Date to">
        message_type = request.POST.get('email')  #email is the name of the name = email in html page
        #<input type="email" name="email" class="form-control" placeholder="email">

        # Initialize the queryset to all messages
        email_inbox = Email_Inbox.objects.all()

        # Filter by message type if provided
        if message_type:
            email_inbox = email_inbox.filter(email=message_type)

        # Filter by date range if both dates are provided
        if date_from and date_to:
            try:
                # Convert dates from string to datetime objects
                date_from = datetime.strptime(date_from, '%Y-%m-%d')
                date_to = datetime.strptime(date_to, '%Y-%m-%d')
                # Ensure the date range is inclusive of both start and end dates
                email_inbox = email_inbox.filter(date__range=[date_from, date_to])
            except ValueError:
                # Handle invalid date format, you can add an error message here if needed
                email_inbox = Email_Inbox.objects.none()

        # Add the filtered queryset to the context and render the template
        context = {
            'email_inbox': email_inbox
        }
        return render(request, self.template_name, context)


class FrontendMessage_detail(UpdateView):
    template_name = 'service/details.html'
    model = Email_Inbox
    context_object_name = 'all'
    fields = ['seen']
    success_url = reverse_lazy('dashBoard_app:dashboard')

    def get(self, request, *args, **kwargs):
        # Retrieve the object and update the `seen` field to True
        self.object = self.get_object()  # Get the instance of the model
        if not self.object.seen:  # If `seen` is False
            self.object.seen = True
            self.object.save()  # Save the change to the database

        # Proceed with the normal get behavior (rendering the form)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_url'] = reverse_lazy('dashBoard_app:mail')
        context['heading'] = "Frontend Message"
        return context


class DeleteFrontendMessage(DeleteView):
    template_name = 'service/delete_service.html'
    model = Email_Inbox
    success_url = reverse_lazy('dashBoard_app:mail')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:mail')
        context['heading'] = "Frontend Message"
        return context


#####################################################################################################
class Settings_for_setting(ListView):
    template_name = 'management/settings.html'
    model = Settings
    context_object_name = 'all'


class UpdateSettings(UpdateView):
    template_name = 'management/updatesettings.html'
    model = Settings
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:settings')
    context_object_name = 'settings'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs.get('pk')
    #     context['custom_url'] = reverse_lazy('dashBoard_app:all_hazz_tips')
    #     context['heading'] = "Hazz Tips"
    #     context['haze_m'] = Hazz_Tips.objects.get(pk=pk)
    #     return context


###################################################################
class All_Form(ListView):
    template_name = 'service/form/all_form.html'
    model = Form
    context_object_name = 'all'


class EditAll_Form(UpdateView):
    template_name = 'service/edit_service.html'
    model = Form
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_forms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['custom_url'] = reverse_lazy('dashBoard_app:all_forms')
        context['heading'] = "Form "
        context['haze_m'] = Form.objects.get(pk=pk)
        return context


class DeleteAll_Form(DeleteView):
    template_name = 'service/delete_service.html'
    model = Form
    success_url = reverse_lazy('dashBoard_app:all_forms')
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_forms')
        context['heading'] = " Form"
        return context


class All_Form_detail(DetailView):
    template_name = 'service/details.html'
    model = Form
    context_object_name = 'all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_forms')
        context['heading'] = "Form"
        return context


class AddAll_Form(CreateView):
    template_name = 'service/add_service.html'
    model = Form
    fields = '__all__'
    success_url = reverse_lazy('dashBoard_app:all_forms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['custom_url'] = reverse_lazy('dashBoard_app:all_forms')
        context['heading'] = "Form"
        return context
