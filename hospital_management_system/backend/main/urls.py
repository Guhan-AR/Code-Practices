# main/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # All API URLs are now neatly under '/api/'
    path('api/auth/', include('Login.urls')),
    path('api/', include('Doctor.urls')), # Assuming Doctor is another app with urls.py

    # JWT Token URLS (also under /api/)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]