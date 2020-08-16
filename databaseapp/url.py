from rest_framework import routers
from databaseapp import views
from django.conf.urls import url
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'user', views.UserViewset)
router.register(r'userinfo', views.UserInfoViewset)
urlpatterns = [
    path('', include(router.urls))
]
