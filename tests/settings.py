INSTALLED_APPS = ["django_svcs"]
MIDDLEWARE = ["django_svcs.middleware.request_container"]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
