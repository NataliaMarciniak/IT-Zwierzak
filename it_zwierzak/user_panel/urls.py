from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = {
    path('admin/', admin.site.urls),
    path('user_panel/', include('user_panel.urls')),
    path('edit/', views.edit, name='edit'),
}

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)