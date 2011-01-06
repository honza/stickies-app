from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


note_states = (
    ('To Do', 'To Do',),
    ('In Progress', 'In Progress',),
    ('Document', 'Document',),
    ('Test', 'Test',),
    ('Verify', 'Verify',),
    ('Done', 'Done',),
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


class Note(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    state = models.CharField(choices=note_states, max_length=13,
        default='To Do')

    def __unicode__(self):
        return self.content


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = UserProfile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
