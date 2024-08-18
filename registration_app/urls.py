from django.urls import path
from registration_app import views

app_name = 'registration_app'

urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('all-user/', views.all_user, name='all_user'),
    path('create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('create-same-user/', views.create_same_user, name='create_same_user'),
]
