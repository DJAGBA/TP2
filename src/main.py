import json
import os
import boto3

TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

def lambda_handler(event, context):
    print("Event: ", json.dumps(event))
    
    client = boto3.resource('dynamodb')
    table = client.Table(TABLE_NAME)
    
    for r in event.get("Records", []):
        if "s3" in r:
            filename = r["s3"]["object"]["key"]
            print(filename)        
            
            # Check database if filename exists
            response = table.get_item(Key={"PK": filename})
            
            if "Item" in response:
                print(f"Le fichier {filename} existe deja.")
            else:
                item = {"PK": filename, "filename": filename}
                table.put_item(Item=item)
                print(f"Item {item}")
                
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda loaded from src/main.py!')
    }