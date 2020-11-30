from django.urls import include,path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'planets',views.PlanetViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('register',views.UserCreate.as_view()),
    path('api-token-auth',obtain_auth_token,name='api_token_auth')
]