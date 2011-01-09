from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models import Note, Project
from django.shortcuts import render_to_response, get_object_or_404
import simplejson as json


STATES = ['todo', 'inprogress', 'document', 'test', 'verify', 'done']


def index(request):
    if request.user.is_authenticated():
        projects = Project.objects.all()
    else:
        projects = None
    return render_to_response('index.html', {'projects': projects},
            context_instance=RequestContext(request))

@login_required
def project(request, id):
    project = Project.objects.get(id=id)
    group = get_object_or_404(Group, name=project.name)
    if group not in request.user.groups.all():
        raise Http404
    return render_to_response('project.html', {'project': project})

@login_required
def ajax(request):
    r = _ajax(request)
    return HttpResponse(json.dumps(r))

def _ajax(request):
    """Wrapper"""
    if not request.is_ajax():
        return {'status': 403}
        
    a = request.POST.get('a')
    if a not in ['move', 'edit', 'delete', 'new']:
        return {'status': 403}
    
    if a in ['move', 'edit', 'delete']:
        n = request.POST.get('note')
        id = int(n[5:])
        note = get_object_or_404(Note, pk=id)
        try:
            note = Note.objects.get(pk=id)
        except ObjectDoesNotExist:
            return {'status': 403}

    if a in ['edit', 'new']:
        content = request.POST.get('content')

    if a == 'move':
        st = request.POST.get('section')
        if st not in STATES:
            return {'status': 403}
        note.state = st
    elif a == 'delete':
        note.delete()
        return {'status': 200}
    elif a == 'new':
        p = request.POST.get('project')
        p = get_object_or_404(Project, id=p)
        note = Note(
            content=content,
            author=request.user,
            project=p)
        note.save()
        return {
            'status': 200,
            'content': _note(note)
        }
    else:
        note.content = content
    note.save()
    return {'status': 200}

def _note(note):
    t = """
<div id="note-%d" class="portlet ui-widget ui-widget-content ui-helper-clearfix ui-corner-all"><div class="portlet-header ui-widget-header ui-corner-all"><span class="ui-icon ui-icon-close"></span><span class="ui-icon ui-icon-pencil"></span></div>
    <div class="portlet-content">%s</div>
    <div class="portlet-meta">
        <p>Author: %s</p>
    </div>
</div>
"""
    n = t % (note.id, note.content, note.author.username,)
    return n
