import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds145273.mlab.com:45273/books

host = "ds145273.mlab.com"
port = 45273
db_name = "books"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
