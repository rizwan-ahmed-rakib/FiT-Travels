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
    # crud image gallery----------------------------------------------------start
    path('image/create/', views.image_create_view, name='image_create'),  # Create a new image
    path('image/update/', views.image_update_view, name='image_update'),  # Update an image
    path('image/detail/', views.image_detail_view, name='image_detail'),  # Get details of an image for editing
    path('image/delete/', views.image_delete_view, name='image_delete'),  # Delete an image
    # crud image gallery----------------------------------------------------End
    # crud video gallery----------------------------------------------------End
    path('video/create/', views.video_create_view, name='video_create'),  # Create a new video
    path('video/update/<int:pk>/', views.video_update_view, name='video_update'),  # Update an existing video
    path('video/delete/<int:pk>/', views.video_delete_view, name='video_delete'),  # Delete a video
    path('video/detail/<int:pk>/', views.video_detail_view, name='video_detail'),  # Get details of a video
    # crud image gallery----------------------------------------------------End

]
