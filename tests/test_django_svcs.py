import pytest
from django.core.exceptions import ImproperlyConfigured

from django_svcs import apps


def test_requires_middleware(settings):
    settings.MIDDLEWARE = []
    with pytest.raises(ImproperlyConfigured):
        apps.SvcsConfig("django_svcs", apps).ready()


def test_get_registry():
    assert apps.get_registry() is not None
