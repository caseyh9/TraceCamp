from django.contrib import admin
from django.urls import include, path
from kickstart.views import get_kickstarter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/kickstarter/<int:kick_id>/', get_kickstarter),
]
