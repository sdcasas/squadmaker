from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.joker.views import api_joker, JokerViewSet


router = DefaultRouter()
router.register('list', JokerViewSet, basename='joker_list')


urlpatterns = [
    path('', include(router.urls)),
    path('api_joker/', api_joker, name='joker_random'),
    path('api_joker/<slug:joker_type>', api_joker, name='joker_type'),
    #path('api_joker/<int:number>/detail', api_joker, name='joker_detail'),
    path('api_joker/<int:number>/edit', api_joker, name='joker_edit'),


]
