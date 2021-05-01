import json
from objectpath import Tree

def my_response2(arg1, arg2):
    print(arg1, arg2)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "bye world"
        }),
    }
    responseTree = Tree(response) # Using a third party lib (objectpath) inside my layer functions
    print(responseTree.execute('$.statusCode'))
    return response