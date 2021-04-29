import json
import pymongo

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    db = pymongo.MongoClient(
        host='mongodb.default.svc.cluster.local',
        port=27017,
        username='admin',
        passwword='admin'
        )
    obj = json.loads(req)
    db.duolingo.dumps.insert_one(obj)
    db.close()

    return len(req)
