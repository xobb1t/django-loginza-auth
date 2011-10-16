from .settings import CONFIG


def widget_id(request):
    return {'LOGINZA_WIDGET_ID': CONFIG['WIDGET_ID']}
