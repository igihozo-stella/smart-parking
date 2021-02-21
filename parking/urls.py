from django.conf.urls import url, include
from django.conf import settings
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^api/location', views.LocationList.as_view()),
    url(r'^api/lot', views.LotList.as_view(),name='api-lot'),
    url(r'^api/block', views.BlockList.as_view(),name='api-block'),
    url(r'^api/slot', views.SlotList.as_view(),name='api-slot'),
    url(r'^api/profile', views.ProfileList.as_view(),name='api-profile'),
    url(r'^api/reservation', views.ReservationList.as_view(),name='api-reservation'),
    url(r'^api/slip', views.SlipList.as_view(),name='api-slip'),
    url(r'^api-token-auth/', obtain_auth_token)

]