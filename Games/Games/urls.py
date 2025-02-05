
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Games API Title",
      default_version="v1",
      description="Your API description",
      terms_of_service="https://example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="Привет друг"),
   ),
   public=True
)


urlpatterns = [
    path('api/', include('Games_app.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='Games API'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]
