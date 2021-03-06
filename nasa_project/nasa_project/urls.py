"""nasa_project URL Configuration

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
from nasa_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Create
    path('nasa/create', views.comment_create),
    # Detail
    path('nasa/detail/<int:nasa_id>', views.comment_detail),
    # list
    path('nasa/list', views.comment_list),
    # Date Picker
    path('nasa/date_picker', views.date_picker),
]
