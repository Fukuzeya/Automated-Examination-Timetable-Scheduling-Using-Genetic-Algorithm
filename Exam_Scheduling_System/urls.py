from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Management.urls',namespace='management')),
    path('scheduling/',include('Scheduling.urls',namespace='scheduling')),
    path('accounts/',include('Accounts.urls',namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
