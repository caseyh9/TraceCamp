from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from generic_app.models import NasaComment
from django.urls import reverse_lazy
from django.http import HttpResponse

class NasaCommentCreateView(CreateView):
    model = NasaComment
    fields = ['comment', 'rating', 'image_url', 'date']

class NasaCommentUpdateView(UpdateView):
    model = NasaComment
    fields = ['comment', 'rating', 'image_url', 'date']
    template_name_suffix = 'comment_update'

class NasaCommentDetailView(DetailView):
    model = NasaComment
    fields = ['comment', 'rating', 'image_url', 'date']
    pk_url_kward = "id"
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        return HttpResponse('Response for get.')

class NasaCommentListView(ListView):
    model = NasaComment


class NasaCommentDeleteView(DeleteView):
    model = NasaComment
    success_url = reverse_lazy('comment_list')
    fields = ['comment', 'rating', 'image_url', 'date']
    pk_url_kward = "id"
