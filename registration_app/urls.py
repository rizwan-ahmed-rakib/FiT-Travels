from django.urls import path
from registration_app import views

app_name = 'registration_app'

urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('all-user/', views.all_user, name='all_user'),
    path('create-test-user/', views.add_demo_user, name='create_test_user'),
    path('create-same-user/', views.create_same_user, name='create_same_user'),
    path('create-user/', views.add_forTest_user, name='create_user'),
    path('edit-user/<int:pk>/', views.EditUserView.as_view(), name='edit_user'),
    path('delete-user/<int:pk>', views.DeleteUserView.as_view(), name='delete_user'),
    path('update-user/<int:pk>', views.EditUserProfileView.as_view(), name='update_user'),
]
