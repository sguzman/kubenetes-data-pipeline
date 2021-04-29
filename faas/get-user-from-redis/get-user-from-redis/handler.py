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

    user = str(r.lpop('users'))

    return json.dumps({
        "user": user
    })
