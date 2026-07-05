import json
import allure
from allure_commons.types import AttachmentType
from requests import Response


def add_api_request(method: str, url: str, params=None, body=None):
    request_data = {"method": method,
                    "url": url,
                    "params": params,
                    "body": body
                    }

    allure.attach(
        body=json.dumps(
            request_data,
            ensure_ascii=False,
            indent=2,
            default=str,
        ),
        name="API request",
        attachment_type=AttachmentType.JSON,
    )


def add_api_response(response: Response):
    try:
        body = response.json()
    except ValueError:
        body = response.text

    response_data = {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": body
    }

    allure.attach(
        body=json.dumps(
            response_data,
            ensure_ascii=False,
            indent=2,
            default=str,
        ),
        name="API response",
        attachment_type=AttachmentType.JSON
    )
