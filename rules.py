import json
import os
import re
from http import HTTPStatus
from typing import List, Optional

import requests
from dotenv import load_dotenv
from flask import Response, jsonify, make_response, request

from consts import PORT, Header
from pokedex import pokedex_pb2
from request import message_to_json, modify_headers

load_dotenv()


def get_rules() -> List[dict]:
    path = os.getenv("POKEPROXY_CONFIG", "rules_config.json")
    with open(path, "r") as file:
        return json.load(file).get("rules")


def matched_rule(message: pokedex_pb2, rules: List[dict]) -> Optional[dict]:
    if not rules:
        return

    for rule in rules:
        match = True

        for condition in rule.get("match"):
            attribute, operator, value = re.split(r"\s*([<>=!]+)\s*", condition)
            attribute = getattr(message, attribute.strip())
            if not attribute:
                match = False
                break

            value = value.strip()
            if value.isdigit():
                value = int(value)

            if operator == "==":
                match = attribute == value
            elif operator == "!=":
                match = attribute != value
            elif operator == ">":
                match = attribute > value
            elif operator == "<":
                match = attribute < value
            else:
                match = False
            if not match:
                break
        if match:
            print(f"Request matched rule: {rule.get('reason')}")
            return rule


def rule_response(rule, message):
    destination_response = handle_destination(rule, message)
    if destination_response.status_code == HTTPStatus.OK:
        return jsonify(destination_response.json())
    return make_response(
        f"The destination {destination_response.url} returned the following error: {destination_response.text}",
        destination_response.status_code,
    )


def handle_destination(rule: dict, message: pokedex_pb2.Pokemon) -> Response:
    destination = get_destination(rule.get("url"))
    if (
            not destination
    ):  # if destination isn't valid / destination unresponsive - the relevant error will be returned
        return make_response("destination URL not provided", HTTPStatus.BAD_REQUEST)
    headers = modify_headers(rule)
    destination_response = requests.post(
        destination, headers=headers, json=message_to_json(message)
    )

    return destination_response


def get_destination(url: str) -> str:
    if request.headers.get(Header.IS_LOCAL_TEST.value) and url:
        endpoint = url.split("/")[-1] if url.split("/") else ""
        return f"http://127.0.0.1:{PORT}/{endpoint}"
    return url
