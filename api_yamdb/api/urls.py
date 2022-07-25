from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet,
                       signup_post, token_post)


router = DefaultRouter()

router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'titles/(?P<titles_id>[^/.]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<titles_id>[^/.]+)/reviews/(?P<reviews_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('auth/signup/', signup_post),
    path('auth/token/', token_post),
    path('', include(router.urls)),
]
