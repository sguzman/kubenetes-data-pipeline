import json
import redis

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = redis.Redis(
            host='redis-master.default.svc.cluster.local',
            port=6379
            )

    user: str = str(r.lpop('users'))
    js_obj = {
        "user": user
    }

    return json.dumps(js_obj)
