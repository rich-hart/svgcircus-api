from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from users.views import UserViewSet
from actors.views import (
    ActorViewSet, 
    ColorViewSet,
    PositionViewSet,
)

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'positions', PositionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^$', schema_view),
]
