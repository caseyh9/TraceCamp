from django.shortcuts import render
from nasa_project import urls
from django.http import HttpResponse
from models import NasaComment

# Create your views here.
def comment_create(request):
    # object create statement ???
    nasa_comment = NasaComment.objects.create(
        comment = request.POST.get('comment'),
        date = request.POST.get('date'),
        rating = request.POST.get('rating')
    )
    # argument ???
    return HttpResponse(nasa_comment)

def comment_detail(request):
    nasa_comment = request.POST.get('nasa_comment')
    # FIXME what should the tag be???
    return HttpResponse(nasa_comment)

def comment_list(request):
    pass

def date_picker(request):
    date = requests.POST.get('date')
    return # Where does this go? FIXME
