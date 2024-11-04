import djp


@djp.hookimpl
def installed_apps():
    return ["django_svcs"]


@djp.hookimpl
def urlpatterns():
    return []


@djp.hookimpl
def settings(current_settings) -> None:
    # find django_svcs in INSTALLED_APPS and move it so it's right after django.contrib.sessions
    installed_apps = current_settings["INSTALLED_APPS"]
    try:
        insert_index = installed_apps.index("django.contrib.sessions")
    except ValueError:
        insert_index = None

    if insert_index is not None:
        installed_apps.remove("django_svcs")

        installed_apps.insert(insert_index + 1, "django_svcs")


@djp.hookimpl
def middleware():
    return [
        djp.After("django.contrib.sessions.middleware.SessionMiddleware"),
        "django_svcs.middleware.request_container",
    ]
