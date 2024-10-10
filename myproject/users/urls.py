from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView
from .views import SignupView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
