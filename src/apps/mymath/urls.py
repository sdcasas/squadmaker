from django.urls import path

from apps.mymath.views import increase_one, minimum_common

urlpatterns = [
    path('increase_one', increase_one, name='increase_one'),
    path('minimum_common', minimum_common, name='minimum_common'),
]
