from django.shortcuts import render, redirect
from calendar_app.models import Event
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse

class CalendarListView(ListView):
    model = Event

class CalendarCreateView(CreateView):
    model = Event
    fields = ['date','time','description']
    success_url = reverse_lazy('list_event')
    #def post(self, request, *args, **kwargs):
    #    return reverse_lazy('detail_event', {'id':self.objects.id})

class CalendarListDay(View):
    def get(self, request):
        day_list = [this_event for this_event in Event.objects.all() if this_event.date == day]
        return render('calendar/list_day', {'day_list':day_list})

class CalendarUpdateView(UpdateView):
    model = Event
    pk_url_kwarg = "id"
    fields = ['date','time','description']
    template_name_suffix = 'update_event'

class CalendarDetailView(DetailView):
    model = Event
    pk_url_kwarg = "id"
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        return render('detail_event', {'id':id})

class CalendarDeleteView(DeleteView):
    model = Event
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list_event')
