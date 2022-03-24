from requests import get
import json

# Opening JSON file with variables
f = open("./variables.json")

# returns JSON object as
# a dictionary
variables = json.load(f)

host = variables["host"]
auth = (variables["user"], variables["password"])
index_name = variables["index"]

# Document with index 1
id = 1

url = "{}{}/_doc/{}".format(host, index_name, id)

response = get(url, auth=auth)

if response.ok:
    content = json.loads(response.content.decode('utf-8'))
    print(content['_source'])