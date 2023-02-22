from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('projects/', include('projects.urls')),
                  path('users/', include('users.urls')),
                  path('forums/', include('forum_app.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
