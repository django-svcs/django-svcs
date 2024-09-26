import djp


@djp.hookimpl
def installed_apps():
    return ["django_svcs"]


@djp.hookimpl
def urlpatterns():
    return []


@djp.hookimpl
def settings(current_settings): ...


@djp.hookimpl
def middleware():
    return [
        djp.After("django.contrib.sessions.middleware.SessionMiddleware"),
        "django_svcs.middleware.request_container",
    ]
