import logging
from app.services.torbot.helpers.validate_user import validate_user
from app.services.torbot.helpers.generate_response import generate_response


def catch_incoming_messages(data):
    if bool(data.message):
        auth = validate_user(data.message.get("from"))
    if bool(data.callback_query):
        auth = validate_user(data.callback_query.get("from"))

    generate_response(auth,data)