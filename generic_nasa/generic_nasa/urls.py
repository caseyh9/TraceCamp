"""generic_nasa URL Configuration

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
from generic_app.views import NasaCommentDetailView, NasaCommentListView, NasaCommentCreateView, NasaCommentUpdateView, NasaCommentDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasa/comment_create', NasaCommentCreateView.as_view(), name='comment_create'),
    path('nasa/comment_list', NasaCommentListView.as_view(), name='comment_list'),
    path('nasa/comment_update/<int:id>/', NasaCommentUpdateView.as_view(), name='comment_update'),
    path('nasa/comment_detail/<int:id>/', NasaCommentDetailView.as_view(), name='comment_detail'),
    path('nasa/comment_delete/<int:id>', NasaCommentDeleteView.as_view(), name='comment_delete'),
]
