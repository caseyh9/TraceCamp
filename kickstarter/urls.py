from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('kick/', include('kick.urls')),
    path('admin/', admin.site.urls),
]
