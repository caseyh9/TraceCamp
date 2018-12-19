from django.shortcuts import render
from nasa_project import urls
from django.http import HttpResponse

# Create your views here.
def comment_create(request):
    pass

def comment_detail(request):
    pass

def comment_list(request):
    pass

def date_picker(request):
    r = requests.get('https://nasa/date_picker')
    HttpResponse(r)
