from django.http import HttpResponse, Http404
from models import Note, Project
from django.shortcuts import render_to_response, get_object_or_404


STATES = ['todo', 'inprogress', 'document', 'test', 'verify', 'done']


def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', {'projects': projects})

def project(request, id):
    project = Project.objects.get(id=id)
    return render_to_response('project.html', {'project': project})

def ajax(request):
    if not request.is_ajax():
        raise Http404
    a = request.POST.get('a')
    if a not in ['move', 'edit', 'delete']:
        raise Http404
    n = request.POST.get('note')
    id = int(n[5:])
    note = get_object_or_404(Note, pk=id)
    if a == 'move':
        st = request.POST.get('section')
        if st not in STATES:
            raise Http404
        note.state = st
    elif a == 'delete':
        note.delete()
        return HttpResponse('OK')
    else:
        content = request.POST.get('content')
        note.content = content
    note.save()
    return HttpResponse('OK')

