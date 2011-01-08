# admin

from django.contrib import admin
from models import Project, Note, UserProfile


class NoteAdmin(admin.ModelAdmin):
    exclude = ('author', 'last_changed_by',)


class ProjectAdmin(admin.ModelAdmin):
    exclude = ('group',)


admin.site.register(Note, NoteAdmin)
admin.site.register(Project, ProjectAdmin)
