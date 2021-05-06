from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.product.urls")),
    path('', include("apps.account.urls")),
    path('rest-auth/', include('rest_auth.urls')),
    

]
