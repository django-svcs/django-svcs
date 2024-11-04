import os

import pytest


@pytest.fixture(autouse=True, name="settings_module", scope="session")
def settings_module() -> None:
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"


@pytest.fixture(autouse=True, name="settings", scope="session")
def _settings(settings_module):
    import django
    from django.conf import settings

    django.setup()

    return settings


@pytest.fixture(scope="function", autouse=True)
def _dj_autoclear_mailbox() -> None:
    # Override the `_dj_autoclear_mailbox` test fixture in `pytest_django`.
    # This works around https://github.com/pytest-dev/pytest-django/issues/993
    pass
