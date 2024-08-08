from django.urls import path, reverse
from dashboard_app import views

app_name = 'dashBoard_app'
urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),
    path('image-gallery/', views.ImageGallery.as_view(), name='image_gallery'),
    path('videos/', views.videoGallery.as_view(), name='videos'),
    path('home-slides/', views.HomeSlide.as_view(), name='home_slides'),
    path('side-slides/', views.SideSlide.as_view(), name='side_slides'),
    path('add-notice/', views.AddNotice.as_view(), name='add_notice'),
    path('all-notice/', views.AllNotice.as_view(), name='all_notice'),
    path('add-about/', views.AddAbout.as_view(), name='add_about'),
    path('all-about/', views.AllAbout.as_view(), name='all_about'),
    path('add-news/', views.AddNews.as_view(), name='add_news'),
    path('all-news/', views.AllNews.as_view(), name='all_news'),
    path('add-speach/', views.AddSpeach.as_view(), name='add_speach'),
    path('all-speach/', views.AllSpeach.as_view(), name='all_speach'),
    path('all-management/', views.AllManagement.as_view(), name='all_management'),
    path('add-management/', views.AddManagement.as_view(), name='add_management'),
    path('mail/', views.FrontendMessage.as_view(), name='mail'),
    path('settings/', views.Settings.as_view(), name='settings'),


]
