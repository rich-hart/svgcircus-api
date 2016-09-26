from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from users.views import UserViewSet
from actors.views import CircleViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'circles', CircleViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
