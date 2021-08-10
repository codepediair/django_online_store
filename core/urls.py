from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def adminnistrator(request):
    return render (request, 'admin_index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/', adminnistrator),
    path('',include('store.urls',namespace='store')),
    path('basket/',include('basket.urls',namespace='basket'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
