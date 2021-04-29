import json
import os

from .lib import duo_data

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    user = json.loads(req["user"])
    return duo_data.get_user(user)
