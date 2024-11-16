from unittest.mock import patch

import pytest
from django.http import HttpRequest, HttpResponse
from django.test import AsyncRequestFactory, RequestFactory

from django_svcs import middleware


@pytest.fixture(name="svcs_from")
def mock_svcs_from():
    with patch("django_svcs.middleware.svcs_from") as mock:
        yield mock


@pytest.fixture(name="sync_view")
def _sync_view():
    def view(request: HttpRequest) -> HttpResponse:
        return HttpResponse(b"Sync response")

    return view


@pytest.fixture(name="async_view")
def _async_view():
    async def view(request: HttpRequest) -> HttpResponse:
        return HttpResponse(b"Async response")

    return view


@pytest.mark.django_db
def test_sync_middleware(svcs_from, sync_view) -> None:
    request = RequestFactory().get("/")
    chain = middleware.request_container(sync_view)
    response = chain(request)

    assert response.content.decode() == "Sync response"
    assert svcs_from.called
    svcs_from.assert_called_with(request)


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_async_middleware(svcs_from, async_view) -> None:
    request = AsyncRequestFactory().get("/")
    chain = middleware.request_container(async_view)
    response = await chain(request)

    assert response.content.decode() == "Async response"
    assert svcs_from.called
    svcs_from.assert_called_with(request)
