# -*- coding:utf-8 -*-
import urllib

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .api import LoginzaError, loginza_api
from .models import Identity
from .signals import post_associate
from .settings import CONFIG


@require_POST
@csrf_exempt
def loginza_callback(request):
    token = request.POST.get('token', None)
    if token is None:
        return http.HttpResponseBadRequest()
    next = request.GET.get('next')
    next = urllib.unquote(next) or '/'
    response = redirect(next)
    try:
        data = loginza_api.get_auth_data(token)
    except LoginzaError:
        messages.error(
            request,
            _(u'There was an error while processing loginza authentication')
        )
        return response

    identity, provider = data['identity'], data['provider']
    user = auth.authenticate(identity=identity, provider=provider)
    if request.user.is_authenticated() and user and request.user != user:
        messages.error(
            request,
            _(u'This OpenID already associated to another account'),
        )
        return response
    if user is None:
        identity = Identity.objects.from_loginza_data(data)
        if request.user.is_authenticated():
            identity.associate(request.user)
            return response
        else:
            username = data.get('nickname') or CONFIG['DEFAULT_USERNAME']
            email = data.get('email', '')
            user = identity.create_user(username, email)
            user.backend = 'loginza.authentication.LoginzaBackend'

    if not user.is_active:
        messages.error(request, _(u'Your account has been disabled'))
    else:
        auth.login(request, user)
        messages.success(request, _(u'Successfull authentication'))
    return response
