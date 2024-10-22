from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Configuração do Swagger para documentação da API
schema_view = get_schema_view(
   openapi.Info(
      title="API de Gerenciamento de Salas",
      default_version='v1',
      description="API para o gerenciamento de espaços e reservas.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('reservas.urls')),       

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
