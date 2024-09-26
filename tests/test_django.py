import pytest
from django.test.client import Client


@pytest.mark.django_db
def test_index_page_200():
    response = Client().get("/")
    assert response.status_code == 200
