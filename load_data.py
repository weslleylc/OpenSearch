from opensearchpy import OpenSearch, RequestsHttpConnection
from os import listdir
from os.path import isfile, join
import json

# Opening JSON file with variables
f = open("./variables.json")

# returns JSON object as
# a dictionary
variables = json.load(f)

host = variables["host"]
auth = (variables["user"], variables["password"])
index_name = variables["index"]

client = OpenSearch(
    hosts=host,
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# # Delete the index.
# response = client.indices.delete(
#     index=index_name
# )

response = client.indices.create(index_name)
print('\nCreating index:')
print(response)


json_local_path = "./data"
onlyfiles = [f for f in listdir(json_local_path) if isfile(join(json_local_path, f))]

for doc_id, file in enumerate(onlyfiles):
    # Opening JSON file
    f = open(join(json_local_path, file))

    # returns JSON object as
    # a dictionary
    document = json.load(f)

    response = client.index(
        index=index_name,
        body=document,
        id=str(doc_id),# you can specify an id or the es you create one for you
        refresh=True
    )
    print(response)