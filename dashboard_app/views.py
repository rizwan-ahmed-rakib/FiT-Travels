from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LoginOutlayer(TemplateView):
    template_name = 'login/loginOutlayer.html'


class DashBoard(TemplateView):
    template_name = 'dashboard/index.html'

class ImageGallery(TemplateView):
    template_name = 'dashboard/imageGallery.html'