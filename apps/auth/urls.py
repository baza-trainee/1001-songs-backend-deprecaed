from django.urls import path

from .views import CustomTokenObtainPairView, CustomTokenRefreshView


from apps.auth.views import AuthRegisterView

urlpatterns = [
    path('', CustomTokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', CustomTokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
]
