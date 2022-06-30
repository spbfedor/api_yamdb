from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', views.signup_post),
    path('v1/auth/token/', views.token_post),
    path('v1/', include(router_v1.urls))

]
