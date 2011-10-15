from django.contrib.auth.models import User

from .models import Identity


class LoginzaBackend(object):

    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, identity=None, provider=None):
        try:
            identity = Identity.objects.get(
                identity = identity,
                provider = provider
            )
        except Identity.DoesNotExist:
            return None
        return identity.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
