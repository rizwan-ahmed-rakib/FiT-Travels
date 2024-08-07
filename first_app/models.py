from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.urls import reverse


# Create your models here.
class Settings(models.Model):
    logoimage = models.ImageField(upload_to='settings/')
    top_link_icon_image = models.ImageField(
        upload_to='settings/', blank=True)  # use it for link inside(which is use inside <head> image/icon image
    baner_image = models.ImageField(upload_to='settings/banerImage/', null=True)
    company_name = models.CharField(max_length=264)
    mobile_number = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    audio = models.FileField(upload_to='settings/', blank=True)
    eye_frame_video = EmbedVideoField(blank=True)
    about_me = models.TextField(max_length=264, null=True)
    address = models.TextField(max_length=264, null=True)
    office_time = models.CharField(max_length=264, null=True)

    def __str__(self):
        return self.company_name


class Nav_Links(models.Model):
    name = models.CharField(max_length=264)


class HomeSlides(models.Model):
    slide_picture = models.ImageField(upload_to='homeslides/')
    title = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.title


class SideHomeSlides(models.Model):
    side_slide_picture = models.ImageField(upload_to='secondSection/')
    title = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.title


class PresidentSpeach(models.Model):
    name = models.CharField(max_length=264)
    designation = models.CharField(max_length=264)
    speach = models.TextField(null=True)
    image = models.ImageField(upload_to='presidentImage/', null=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    image = models.ImageField(upload_to='aboutUs/')
    about_us = models.TextField()
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name


class TopManagement(models.Model):
    name = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    want_to_say = RichTextField(null=True)
    picture = models.ImageField(upload_to='topManagement/', null=True)

    def __str__(self):
        return self.name


class Hazz_Message(models.Model):
    number = models.CharField(max_length=264, blank=True)
    title = RichTextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.number


class HazzMustbeDone(models.Model):
    number = models.CharField(max_length=264, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.number


class Agency_Should(models.Model):
    number = models.CharField(max_length=264, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.number


class Hazz_Tips(models.Model):
    number = models.CharField(max_length=264, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.number


class Image_Gallery(models.Model):
    name = models.CharField(max_length=264, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name


class Video_Gallery(models.Model):
    name = models.CharField(max_length=264, blank=True)
    video = models.FileField(upload_to='gallery/video/', blank=True)
    add_video_from_any_link = EmbedVideoField(blank=True)

    # thumbnail-picture = models.ImageField(upload_to='gallery/thumbnail/', blank=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    subject = models.TextField(blank=True)
    notice_body = RichTextField()
    file = models.FileField(upload_to='notice/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Form(models.Model):
    subject = models.TextField(null=True)
    pub_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='form/', null=True)

    def __str__(self):
        return self.subject


class Email_Inbox(models.Model):
    name = models.CharField(max_length=264, blank=True, )
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('contact_us')


class Latest_news(models.Model):
    headline = models.TextField(null=True)
    picture = models.ImageField(upload_to='news/')
    news_details = RichTextField()
    pub_date = models.DateField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.headline
