import json
import os

from .lib import duo_data

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    js = json.loads(req)
    user = js["user"]
    return duo_data.get_user(user)
