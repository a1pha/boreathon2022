from flask import Flask
from flask_dynamo import Dynamo
import app
import boto3

AWS_ACCESS_KEY_ID = 'AKIAWLU3NUWTE3BD7VN6'
AWS_SECRET_ACCESS_KEY = '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'
REGION_NAME = 'us-east-2'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key= AWS_SECRET_ACCESS_KEY, region_name = REGION_NAME)

table = dynamodb.Table('R3-Account')

# Print out some data about the table.
print(table.item_count)
print(table.creation_date_time)

# Insert dummy data
table.put_item(
   Item={
        'ID': 1,
	'account_num': '10000',
        'balance': 0,
        'account_status': 'open',
    }
)
