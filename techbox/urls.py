from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.product.urls")),
    path('', include("apps.account.urls")),
    path('rest-auth/', include('rest_auth.urls')),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)

