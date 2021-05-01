import json

def my_response1(arg1, arg2):
    print(arg1, arg2)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
    return response