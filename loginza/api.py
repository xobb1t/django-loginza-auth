import hashlib
import requests

from django.utils import simplejson as json
from .settings import CONFIG


class LoginzaError(Exception):

    pass


class LoginzaAPI(object):

    def __init__(self, widget_id=None, secret=None, api_url=None):
        self.widget_id = widget_id
        self.secret = secret
        self.api_url = api_url or 'http://loginza.ru/api/authinfo'

    def make_signature(self, token):
        signature = hashlib.md5(token)
        signature.update(self.secret)
        return signature.hexdigest()

    def get_auth_data(self, token):
        request_data = {'token': token}
        if self.widget_id and self.secret:
            signature = self.make_signature(token)
            request_data.update({'id': self.widget_id, 'sig': signature})
        response = requests.get(self.api_url, params=request_data, timeout=10)
        if response.status_code != 200:
            raise LoginzaError('Request error')
        data = json.loads(response.content)
        if 'error_type' in data:
            print 'error'
            raise LoginzaError(data.get('error_message'))
        return data


loginza_api = LoginzaAPI(
    widget_id = CONFIG['WIDGET_ID'],
    secret = CONFIG['SECRET_KEY'],
    api_url = CONFIG['API_URL'],
)
