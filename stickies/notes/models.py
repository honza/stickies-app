from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


note_states = (
    ('todo', 'To Do',),
    ('inprogress', 'In Progress',),
    ('document', 'Document',),
    ('test', 'Test',),
    ('verify', 'Verify',),
    ('done', 'Done',),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    group = models.ForeignKey(Group, null=True, blank=True)

    def save(self, *args, **kwds):
        g = Group.objects.create(name=self.name)
        self.group = g
        return super(Project, self).save(args, kwds)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='authors')
    project = models.ForeignKey(Project)
    last_changed_by = models.ForeignKey(User, null=True, blank=True)
    state = models.CharField(choices=note_states, max_length=13,
        default='todo')

    def save(self, *args, **kwds):
        if not self.last_changed_by:
            self.last_changed_by = self.author
        super(Note, self).save(args, kwds)

    def __unicode__(self):
        return self.content


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = UserProfile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
