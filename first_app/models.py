from django.db import models


# Create your models here.
class Settings(models.Model):
    logoimage = models.ImageField(upload_to='settings/')
    slider_image = models.ImageField(upload_to='settings/')
    company_name = models.CharField(max_length=264)
    mobile_number = models.CharField(max_length=264)
    email = models.CharField(max_length=264)

    def __str__(self):
        return self.company_name


class Nav_Links(models.Model):
    name = models.CharField(max_length=264)


class HomeSlides(models.Model):
    slide_picture = models.ImageField(upload_to='homeslides/')
    title = models.CharField(max_length=264)
    def __str__(self):
        return self.title
