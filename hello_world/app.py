import json
from mylib1 import my_response1
from mylib2 import my_response2
from objectpath import Tree


def lambda_handler(event, context):
    response = my_response1(1,2)  # Using function from my layer in mylib1 folder
    responseTree = Tree(response) # Using a third party lib (objectpath) defined in my layer requirements.txt
    print(responseTree.execute('$.statusCode'))
    print(my_response2(3,4)) # Using function from my layer in mylib2 folder
    return response
