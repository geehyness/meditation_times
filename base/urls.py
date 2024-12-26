from django.urls import path
from .views import MTList, Message

urlpatterns = [
    path('', MTList.as_view(), name='home'),
    path('message/<int:pk>', Message.as_view(), name='message'),
]
