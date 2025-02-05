from django.urls import path, include
from . import views
from rest_framework import routers
from . views import GameViewSet


router = routers.DefaultRouter()
router.register('games', GameViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),



]

