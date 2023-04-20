from http import HTTPStatus
from dotenv import load_dotenv
import google
from flask import Flask, make_response

from consts import HOST, PORT
from request import (get_response_for_invalid_signature,
                     is_content_in_request_body, is_signature_valid,
                     log_request_with_endpoint_name, parse_message)
from rules import get_rules, matched_rule, rule_response

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return {"message": "Welcome to the Pokemon Streamer!"}


@app.route("/stream", methods=["POST"])
def stream():
    if not is_content_in_request_body():
        return make_response("request body contains no content", HTTPStatus.BAD_REQUEST)

    try:
        message = parse_message()
    except google.protobuf.message.DecodeError:
        return make_response("the message body is not protobuf encoded", HTTPStatus.BAD_REQUEST)

    if not is_signature_valid():
        return get_response_for_invalid_signature()

    rule = matched_rule(message, rules)
    if rule:
        return rule_response(rule, message)
    return {"message": "no rule matched, message not routed to any destination"}


@app.route("/pokeball", methods=["POST"])
def pokeball():
    log_request_with_endpoint_name(pokeball.__name__)
    return {"message": "pokeball, I choose you!"}


@app.route("/catch_em_all", methods=["POST"])
def catch_em_all():
    log_request_with_endpoint_name(catch_em_all.__name__)
    return {"message": "I'm gonna catch 'em all!"}


if __name__ == "__main__":
    rules = get_rules()
    app.run(port=PORT, host=HOST, debug=True)
