from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


admin.site.site_header = "SquadMaker"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Callenger for SquadMaker"

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('api/v1/joker/', include(("joker.urls", "joker"), namespace="joker")),
    path('api/v1/math/', include(("mymath.urls", "mymath"), namespace="mymath")),
]


if settings.ENABLE_SWAGGER:
    schema_view = get_schema_view(
        openapi.Info(
            title="SquadMaker API's",
            default_version='v1',
            description="Callenger squadmaker",
            terms_of_service="Daniel Casas",
        ),
        public=True,
    )
    urlpatterns.append(
        path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    )


if settings.DEBUG:
    pass
    #import debug_toolbar
    #urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
