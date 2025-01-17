from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from backend import views
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls')),
    path('', views.dummy_home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/ ', TokenRefreshView.as_view(), name='token_refresh'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
