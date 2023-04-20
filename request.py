import base64
import hashlib
import hmac
import json
import logging
import os
from http.client import UNAUTHORIZED

from dotenv import load_dotenv
from flask import Response, make_response, request
from werkzeug.datastructures import EnvironHeaders

from consts import Header
from pokedex import pokedex_pb2

load_dotenv()


def is_content_in_request_body() -> bool:
    return bool(request.data)


def get_response_for_invalid_signature() -> Response:
    if not request.headers.get(Header.X_GRD_SIGNATURE.value):
        return make_response("No signature was provided", UNAUTHORIZED)
    return make_response("Invalid signature", UNAUTHORIZED)


def parse_message() -> pokedex_pb2:
    return pokedex_pb2.Pokemon.FromString(request.data)


def is_signature_valid() -> bool:
    secret = base64.b64decode(os.getenv("ENCRYPTION_SECRET"))
    validation_signature = hmac.new(
        secret, request.get_data(), hashlib.sha256
    ).hexdigest()
    x_grd_signature = request.headers.get(Header.X_GRD_SIGNATURE.value)

    return validation_signature == x_grd_signature


def message_to_json(message: pokedex_pb2) -> str:
    message_dict = {}
    for descriptor, value in message.ListFields():
        message_dict[descriptor.name] = value
    return json.dumps(message_dict)


def modify_headers(rule: dict):
    headers = {
        key: value
        for key, value in request.headers.items()
        if key != Header.X_GRD_SIGNATURE.value
    }
    headers[Header.X_GRD_REASON.value] = rule.get("reason")
    request.headers = EnvironHeaders(headers)

    return headers


def log_request_with_endpoint_name(endpoint_name: str):
    logging.info(
        f"{endpoint_name} received: {json.loads(request.get_data().decode('utf-8'))}"
    )
