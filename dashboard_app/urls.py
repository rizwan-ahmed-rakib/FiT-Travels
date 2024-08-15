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
    path('edit-management/<int:pk>/', views.EditMaagement.as_view(), name='edit_management'),
    path('delete-management/<int:pk>/', views.DeleteMaagement.as_view(), name='delete_management'),
    path('details-management/<int:pk>/', views.Maagement_detail.as_view(), name='details_management'),

    path('all-hazz-message/', views.AllHazzMessage.as_view(), name='all_hazz_message'),
    path('edit-hazz-message/<int:pk>/', views.EditHazzMessage.as_view(), name='edit_hazz_message'),
    path('delete-hazz-message/<int:pk>/', views.DeleteHazzMessage.as_view(), name='delete_hazz_message'),
    path('details-hazz-message/<int:pk>/', views.HazzMessage_detail.as_view(), name='details_hazz_message'),
    path('add-hazz-message/', views.AddHazzMessage.as_view(), name='add_hazz_message'),

    path('all-hazz-mustbe-done/', views.AllHazzMustbeDone.as_view(), name='all_hazz_mustbe_done'),
    path('edit-hazz-mustbe-done/<int:pk>/', views.EditHazzMustbeDone.as_view(), name='edit_hazz_mustbe_done'),
    path('delete-hazz-mustbe-done/<int:pk>/', views.DeleteHazzMustbeDone.as_view(), name='delete_hazz_mustbe_done'),
    path('details-hazz-mustbe-done/<int:pk>/', views.HazzMustbeDone_detail.as_view(), name='details_hazz_mustbe_done'),
    path('add-hazz-mustbe-done/', views.AddHazzMustbeDone.as_view(), name='add_hazz_mustbe_done'),

    path('all-agency-should/', views.AllAgencyShould.as_view(), name='all_agency_should'),
    path('edit-agency-should/<int:pk>/', views.EditAgencyShould.as_view(), name='edit_agency_should'),
    path('delete-agency-should/<int:pk>/', views.DeleteAgencyShould.as_view(), name='delete_agency_should'),
    path('details-agency-should/<int:pk>/', views.AgencyShould_detail.as_view(), name='details_agency_should'),
    path('add-agency-should/', views.AddAgencyShould.as_view(), name='add_agency_should'),

    path('all-hazz-tips/', views.AllHazzTips.as_view(), name='all_hazz_tips'),
    path('edit-hazz-tips/<int:pk>/', views.EditHazzTips.as_view(), name='edit_hazz_tips'),
    path('delete-hazz-tips/<int:pk>/', views.DeleteHazzTips.as_view(), name='delete_hazz_tips'),
    path('details-hazz-tips/<int:pk>/', views.HazzTips_detail.as_view(), name='details_hazz_tips'),
    path('add-hazz-tips/', views.AddHazzHazzTips.as_view(), name='add_hazz_tips'),

    path('mail/', views.FrontendMessage.as_view(), name='mail'),
    path('details-frontend-message/<int:pk>/', views.FrontendMessage_detail.as_view(), name='details_frontend_message'),
    path('delete-frontend-message/<int:pk>/', views.DeleteFrontendMessage.as_view(), name='delete_frontend_message'),

    path('settings/', views.Settings_for_setting.as_view(), name='settings'),
    path('edit-settings/<int:pk>/', views.UpdateSettings.as_view(), name='edit_settings'),

    path('all-forms/', views.All_Form.as_view(), name='all_forms'),
    path('edit-all-forms/<int:pk>/', views.EditAll_Form.as_view(), name='edit_all_forms'),
    path('delete-all-forms/<int:pk>/', views.DeleteAll_Form.as_view(), name='delete_all_forms'),
    path('details-all-forms/<int:pk>/', views.All_Form_detail.as_view(), name='details_all_forms'),
    path('add-all-forms/', views.AddAll_Form.as_view(), name='add_all_forms'),

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
    path('homeslides/update/', views.home_slide_update_view, name='update_home_slide'),
    path('homeslide/detail/', views.home_slide_detail_view, name='home_slide_detail'),  # Get details of an image for editing
    path('homeslides/delete/', views.DeleteHomeSlide.as_view(), name='delete_home_slide'),
    # crud notice----------------------------------------------------end
    path('notice/create/', views.notice_create, name='notice_create'),  # Create a new notice
    path('notice/update/', views.notice_update, name='notice_update'),  # Update a notice
    path('notice/detail/', views.notice_detail, name='notice_detail'),  # Get details of a notice for editing
    path('notice/delete/', views.notice_delete, name='notice_delete'),  # Delete a notice
    # crud side slider------------------------------------------------------start
    path('side-slider/create/', views.side_slide_create_view, name='side_lide_create'),  # Create a new notice
    path('side-slider/update/', views.side_slide_update_view, name='side_lide_update'),  # Update a notice
    path('side-slider/detail/', views.side_slide_detail_view, name='side_lide_detail'),
    # Get details of a notice for editing
    path('side-slider/delete/', views.side_slide_delete_view, name='side_lide_delete'),  # Delete a notice
    # crud side slider------------------------------------------------------end
]
