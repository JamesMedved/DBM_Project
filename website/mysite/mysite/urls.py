from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jubi/', include('jubi.urls')),
    path('admin/', admin.site.urls),
]