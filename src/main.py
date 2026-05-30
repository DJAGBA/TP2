import json
import os
import boto3

TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

def lambda_handler(event, context):
    print("Event: ", json.dumps(event))
    for r in event.get("Records"):
        if "object" in r.get("s3"):
            filename = r["s3"]["object"]["key"]
            print(filename)
            
    # Check database if filename exists
    client = boto3.resource('dynamodb')
    
    table = client.Table(TABLE_NAME)
    
    response = table.get_item(Key={"PK": "kdjagba"})
    
    item = {"PK": "KDJAGBA", "filename": "test"}
    table.put_item(Item=item)
    print(f"Item {item}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda loaded from src/main.py!')
    }