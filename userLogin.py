import json

def lambda_handler(event, context):

    return {
            "statusCode": 502,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Content-Type": "application/json"
            },
            "body": json.dumps({"status":"SUCCESS","message": "Hello"})
        }
        