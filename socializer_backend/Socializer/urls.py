from django.urls import path
from .views import ProfileListCreate, ProfileDetail, RegisterView


urlpatterns = [
    path('profiles/', ProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('register/', RegisterView.as_view(), name='register'),

]
