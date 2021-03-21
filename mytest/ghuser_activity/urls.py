from django.urls import path

from ghuser_activity.views import index

urlpatterns = [
    path('', index),
]
