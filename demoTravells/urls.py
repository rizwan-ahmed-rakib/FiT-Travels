"""
URL configuration for demoTravells project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from first_app import views

# app_name = 'demoTravells'

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('abc/', views.HomePageView.as_view(), name='homee'),
                  path('', views.TravellsPageView.as_view(), name='home'),
                  path('travel/', views.TravellsPageView.as_view(), name='travell_home'),
                  path('go/', views.TravellsPageView.as_view(), name='travell_go'),
                  path('about/', views.AboutPageView.as_view(), name='about'),
                  path('management/', views.ManagementPageView.as_view(), name='management'),
                  path('base/', views.BaseView.as_view(), name='base'),
                  path('president-speach/', views.PresidenSpeach.as_view(), name='president_speach'),
                  path('speach/<int:pk>/', views.Speach.as_view(), name='speach'),
                  path('hazz-message/', views.HazzMessage.as_view(), name='hazz_message'),
                  path('hazz-must-be-done/', views.HazzMustBeDone.as_view(), name='hazz_must_be_done'),
                  path('agency-should/', views.AgencyShould.as_view(), name='agency_should'),
                  path('hazz-tips/', views.HazzTips.as_view(), name='hazz_tips'),
                  path('image-gallery/', views.ImageGallery.as_view(), name='image_gallery'),
                  path('video-gallery/', views.VideoGallery.as_view(), name='video_gallery'),
                  path('notice/', views.Notices.as_view(), name='notice'),
                  path('notice-details/<int:pk>/', views.NoticeDetail.as_view(), name='notice-details'),
                  path('form/', views.FormDownload.as_view(), name='form_download'),
                  path('contact-us/', views.ContactUs.as_view(), name='contact_us'),
                  path('news-details/<int:pk>', views.News_details.as_view(), name='news_details'),
                  path('news', views.All_News.as_view(), name='news_all'),
                  # path('login-outlayer/',views.LoginOutlayer.as_view(), name='login_outlayer'),
                  path('dashboard/', views.DashBoard.as_view(), name='dashboard'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
