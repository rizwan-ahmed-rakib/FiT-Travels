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
    path('edit-about/<int:pk>/', views.EditAbout.as_view(), name='edit_about'),
    path('delete-about/<int:pk>/', views.AllAbout_delete.as_view(), name='delete_about'),
    path('add-news/', views.AddNews.as_view(), name='add_news'),
    path('all-news/', views.AllNews.as_view(), name='all_news'),
    path('edit-news/<int:pk>/', views.EditNews.as_view(), name='edit_news'),
    path('delete-news/<int:pk>/', views.DeleteNews.as_view(), name='delete_news'),
    path('details-news/<int:pk>/', views.News_detail.as_view(), name='details_news'),
    path('add-speach/', views.AddSpeach.as_view(), name='add_speach'),
    path('all-speach/', views.AllSpeach.as_view(), name='all_speach'),
    path('edit-speach/<int:pk>/', views.EditSpeach.as_view(), name='edit_speach'),
    path('delete-speach/<int:pk>/', views.DeleteSpeach.as_view(), name='delete_speach'),
    path('details-speach/<int:pk>/', views.Speach_detail.as_view(), name='details_speach'),
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
    path('video/update/', views.video_update_view, name='video_update'),  # Update a video
    path('video/detail/', views.video_detail_view, name='video_detail'),  # Get details of a video for editing
    path('video/delete/', views.video_delete_view, name='video_delete'),  # Delete a video

    # crud home sliders----------------------------------------------------start
    path('homeslides/create/', views.CreateHomeSlide.as_view(), name='create_home_slide'),
    path('homeslides/update/', views.UpdateHomeSlide.as_view(), name='update_home_slide'),
    path('homeslides/delete/', views.DeleteHomeSlide.as_view(), name='delete_home_slide'),
    # crud notice----------------------------------------------------end
    path('notice/create/', views.notice_create, name='notice_create'),  # Create a new notice
    path('notice/update/', views.notice_update, name='notice_update'),  # Update a notice
    path('notice/detail/', views.notice_detail, name='notice_detail'),  # Get details of a notice for editing
    path('notice/delete/', views.notice_delete, name='notice_delete'),  # Delete a notice
    # crud side slider------------------------------------------------------start
    path('side-slider/create/', views.side_slide_create_view, name='side_lide_create'),  # Create a new notice
    path('side-slider/update/', views.side_slide_update_view, name='side_lide_update'),  # Update a notice
    path('side-slider/detail/', views.side_slide_detail_view, name='side_lide_detail'),  # Get details of a notice for editing
    path('side-slider/delete/', views.side_slide_delete_view, name='side_lide_delete'),  # Delete a notice
    # crud side slider------------------------------------------------------end
]
