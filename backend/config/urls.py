from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls')),
    path('api/user/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('blog.urls')),
    path('schema', get_schema_view(
        title="BlogApi",
        description="API for the blog site",
        version="1.0.0"
    ), name='openapi-schema'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)