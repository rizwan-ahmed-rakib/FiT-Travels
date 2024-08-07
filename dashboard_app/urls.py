from django.urls import path, reverse
from dashboard_app import views

app_name = 'dashBoard_app'
urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='dashboard'),
    path('image-gallery/', views.ImageGallery.as_view(), name='image_gallery'),

]
