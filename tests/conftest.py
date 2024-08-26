import os

import pytest


@pytest.fixture(autouse=True, name="settings_module", scope="session")
def settings_module():
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


@pytest.fixture(autouse=True, name="settings", scope="session")
def _settings(settings_module):
    import django
    from django.conf import settings

    django.setup()

    return settings
