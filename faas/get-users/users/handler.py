import atexit
import json
import psycopg2

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    conn = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="postgres-postgresql.default.svc.cluster.local",
                                  port="5432",
                                  database="duolingo")

    def close_conn():
        if conn is not None:
            conn.close()

    atexit.register(close_conn)
    cursor = conn.cursor()
    
    def close_cur():
        if cursor is not None:
            cursor.close()

    atexit.register(close_cur)
    cursor.execute("SELECT username from duolingo.data.users;")
    record = cursor.fetchall()
    array = [a[0] for a in record]
    cursor.close()
    conn.close()

    return json.dumps(array)
