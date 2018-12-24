"""calendar_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calendar_app.views import CalendarListView, CalendarCreateView, CalendarListDay, CalendarUpdateView, CalendarDetailView, CalendarDeleteView
from calendar_app.models import Event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_event', CalendarListView.as_view(), name='list_event'),
    path('create_event', CalendarCreateView.as_view(), name='create_event'),
    path('update_event/<int:id>/', CalendarUpdateView.as_view(), name='update_event'),
    path('detail_event/<int:id>/', CalendarDetailView.as_view(), name='detail_event'),
    path('delete_event/<int:id>/', CalendarDeleteView.as_view(), name='delete_event'),
    path('about/', CalendarListDay.as_view()),
]
