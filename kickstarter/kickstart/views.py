from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from kickstart.models import kickstarter

def get_kickstarter(request, kick_id):
    kick = kickstarter.objects.filter(id = kick_id)
    response = serializers.serialize("json", kick)
    return HttpResponse(response)
