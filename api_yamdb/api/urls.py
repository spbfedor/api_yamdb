from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet, CategoryViewSet, GenreViewSet


router = DefaultRouter()

router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls)),
]
