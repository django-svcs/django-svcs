import asyncio
from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.utils.decorators import sync_and_async_middleware

from .apps import svcs_from

# pyright: reportRedeclaration=false


@sync_and_async_middleware
def request_container(get_response: Callable):
    """Middleware that attaches a service container to the request"""
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request: HttpRequest) -> HttpResponse:
            """
            Asynchronous middleware function which attaches a
            service container to the request.

            """
            with svcs_from(request):
                response = await get_response(request)
                return response

    else:

        def middleware(request: HttpRequest) -> HttpResponse:
            """
            Synchronous middleware function which attaches a
            service container to the request.

            """
            with svcs_from(request):
                response = get_response(request)
                return response

    return middleware
