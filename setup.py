from setuptools import setup, find_packages


setup(
    name = 'loginza',
    version = '0.4.0',
    author = 'Dima Kukushkin',
    author_email = 'dima@kukushkin.me',
    description = 'Django application for Loginza service',
    url = 'https://github.com/xobb1t/django-loginza',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['requests']
)
