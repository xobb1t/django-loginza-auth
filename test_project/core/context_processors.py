from django.contrib.sites.models import RequestSite


def site(request):
    return {'site': RequestSite(request)}


def path(request):
    return {'path': request.path}
