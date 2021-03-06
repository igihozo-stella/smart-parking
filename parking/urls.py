from django.conf.urls import url, include
from django.conf import settings
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterApi, LoginView

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^api/login', LoginView.as_view(),name='api-login'),
    url(r'^django-sb-admin/login/',views.login,name='login'),
    url(r'^api/register', RegisterApi.as_view(),name='api-register'),
    url(r'^api/location', views.LocationList.as_view(),name='api-location'),
    url(r'^api/block', views.BlockList.as_view(),name='api-block'),
    url(r'^api/slot', views.SlotList.as_view(),name='api-slot'),
    url(r'^api/profile', views.ProfileList.as_view(),name='api-profile'),
    url(r'^api/reservation', views.ReservationList.as_view(),name='api-reservation'),
    url(r'^api/slip', views.SlipList.as_view(),name='api-slip'),
    url(r'api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]