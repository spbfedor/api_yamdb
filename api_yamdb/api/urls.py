from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', views.APISignUp.as_view()),
    path('v1/auth/token/', views.APIToken.as_view()),
    path('v1/', include(router_v1.urls))
    # TODO Нужна своя страница "me"?
]
