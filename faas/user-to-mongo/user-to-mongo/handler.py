import json
import pymongo

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    db = pymongo.MongoClient(host='redis-master.default.svc.cluster.local', port=27017)
    obj = json.loads(req)
    db.duolingo.dumps.insert_one(obj)
    db.close()

    return len(req)
