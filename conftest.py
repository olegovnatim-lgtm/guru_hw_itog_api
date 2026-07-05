import logging
import sys
import pytest
import os

from api.base_api import BaseApi
from api.location_api import LocationApi
from config import API_BASE_URL
from data.location_data import location_request
from models.location import CreateLocationResponse, CreateLocationRequest


def pytest_configure(config):
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)-25s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(
                "logs/test.log",
                encoding="utf-8",
            ),
        ],
        force=True,
    )


@pytest.fixture()
def base_api():
    api = BaseApi(base_url=API_BASE_URL)
    yield api
    api.session.close()


@pytest.fixture()
def location_api(base_api):
    return LocationApi(api=base_api)


@pytest.fixture
def created_location(location_api) -> tuple[CreateLocationResponse, CreateLocationRequest]:
    request_body = location_request()
    response = location_api.create(request_body)
    assert response.status_code == 200
    response_body = CreateLocationResponse.model_validate(response.json())
    return response_body, request_body
