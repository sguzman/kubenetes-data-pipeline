import pymongo

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    db = pymongo.MongoClient(host='redis-master.default.svc.cluster.local', port=27017)
    db.duolingo.dumps.insert_one(req)
    db.close()

    return req
