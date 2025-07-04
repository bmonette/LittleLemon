from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuViewSet, basename='menu')
router.register(r'booking/tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
