from django.db import models


# Create your models here.
class Settings(models.Model):
    logoimage = models.ImageField(upload_to='settings/')
    slider_image = models.ImageField(upload_to='settings/')  # use it for link image/icon image
    company_name = models.CharField(max_length=264)
    mobile_number = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    audio = models.FileField(upload_to='settings/', blank=True)
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
