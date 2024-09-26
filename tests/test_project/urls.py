from django.http import HttpResponse
import djp
from django.urls import path

urlpatterns = [
    path("", lambda request: HttpResponse("Hello world"))
] + djp.urlpatterns()
