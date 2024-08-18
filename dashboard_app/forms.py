from django import forms
from ckeditor.widgets import CKEditorWidget
from bootstrap_modal_forms.forms import BSModalModelForm
from first_app.models import Image_Gallery, Video_Gallery, Notice, AboutUs


class ImageGalleryForm(BSModalModelForm):
    class Meta:
        model = Image_Gallery
        fields = ['name', 'image']


class VideoGalleryForm(BSModalModelForm):
    class Meta:
        model = Video_Gallery
        fields = ['name', 'video', 'add_video_from_any_link']


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['subject', 'notice_body', 'file']


# class AboutUsForm(forms.ModelForm):
#     about_us = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = AboutUs
#         fields = ['image', 'name', 'about_us']
