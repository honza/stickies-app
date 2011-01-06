from django.http import HttpResponse
from models import Note, Project
from django.shortcuts import render_to_response


def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', {'projects': projects})

def project(request, id):
    return HttpResponse('Id %s' % id)

def ajax(request):
    pass