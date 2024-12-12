from django.urls import path
from .views import ProfileListCreate, ProfileDetail, RegisterView, LoginView


urlpatterns = [
    path('profiles/', ProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail-id'),
    path('profiles/<str:username>/',
         ProfileDetail.as_view(), name='profile-detail-username'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]
