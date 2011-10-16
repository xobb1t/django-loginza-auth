from django.contrib.auth.models import User
from django.db import models
from django.utils import simplejson as json

from .signals import post_associate


class IdentityManager(models.Manager):

    def from_loginza_data(self, loginza_data):
        data = json.dumps(loginza_data)
        identity, created = self.get_or_create(
            identity = loginza_data['identity'],
            provider = loginza_data['provider'],
            defaults = {'data': data}
        )
        if not created:
            identity.data = data
            identity.save()
        return identity


class Identity(models.Model):

    identity = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True)
    data = models.TextField()

    objects = IdentityManager()

    class Meta:
        unique_together = (('identity', 'provider'),)

    def associate(self, user):
        self.user = user
        self.save()
        post_associate.send(sender=type(self), instance=self)

    def create_user(self, username, email, password=None):
        existing_users = 0
        new_username = None
        while True:
            existing_users += 1
            qs = User.objects.all()
            qs = qs.filter(username=new_username or username)
            if not qs.exists():
                break
            new_username = '%s_%d' % (username, existing_users)
        user = User.objects.create_user(new_username or username, email, password)
        self.associate(user)
        return user
