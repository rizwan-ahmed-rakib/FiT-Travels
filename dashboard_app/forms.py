from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from first_app.models import Image_Gallery, Video_Gallery


class ImageGalleryForm(BSModalModelForm):
    class Meta:
        model = Image_Gallery
        fields = ['name', 'image']


class VideoGalleryForm(BSModalModelForm):
    class Meta:
        model = Video_Gallery
        fields = ['name', 'video', 'add_video_from_any_link']
