from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from nasa_app.models import NasaComment
import requests
from django.shortcuts import redirect
from django.utils.dateparse import parse_date

# Create your views here.
def comment_create(request):
    if (request.method == "GET"):
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        date = request.GET.get("date")
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]
        return render(request, 'create.html', {'image_url':url, 'date':date})
    elif (request.method == "POST"):
        nasa_comment = NasaComment.objects.create(
            comment = request.POST.get('comment'),
            rating = request.POST.get('rating'),
            date = parse_date(request.POST.get('date'))
        )
        return redirect('/nasa/detail/' + str(nasa_comment.id), {'nasa_comment':nasa_comment})
    else:
        return HttpResponse('Nope.')

def comment_detail(request, nasa_id):
    nasa_comment = NasaComment.objects.get(id = nasa_id)
    return render(request, 'detail.html', {'nasa_comment':nasa_comment})

def comment_list(request):
    nasa_comments = NasaComment.objects.all()
    return render(request, 'list.html', {'nasa_comments':nasa_comments})

def date_picker(request):
    if (request.method == "GET"):
        return render(request, 'date_picker.html')
    elif (request.method == "POST"):
        return redirect(f'/nasa/create?date={request.POST.get("date")}')
    else:
        return HttpResponse("Nah.")
