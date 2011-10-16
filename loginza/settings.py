from django.conf import settings


CONFIG = {
    'WIDGET_ID': None,
    'SECRET_KEY': None,
    'API_URL': None,
    'DEFAULT_USERNAME': 'loginza_user',
}
CONFIG.update(getattr(settings, 'LOGINZA_CONFIG', {}))
