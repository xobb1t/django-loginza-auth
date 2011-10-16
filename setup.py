import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name = 'django-loginza-auth',
    version = '0.1.1',
    license = 'ISC',
    description = 'Loginza.ru API client',
    long_description = read('README.rst'),
    author = 'Dima Kukushkin',
    author_email = 'dima@kukushkin.me',
    url = 'https://github.com/xobb1t/django-loginza-auth',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['requests'],
)
