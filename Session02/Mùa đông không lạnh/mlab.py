import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds127153.mlab.com:27153/hotwinter

host = "ds127153.mlab.com"
port = 27153
db_name = "hotwinter"
user_name = "admin1"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
