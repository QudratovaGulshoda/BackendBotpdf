from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router =  DefaultRouter()
router.register('users',BotUserViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('info/',BotUserInfo.as_view()),
    path('count/',BotUserCount.as_view()),
]