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

    items = json.loads(req)
    for i in items:
        r.rpush('users', i)

    return len(items)
