import djp

INSTALLED_APPS = []
MIDDLEWARE = []
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

ROOT_URLCONF = "tests.test_project.urls"

djp.settings(globals())
