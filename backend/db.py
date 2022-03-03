from flask import Flask
from flask_dynamo import Dynamo
from app.py import app #fix this import

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

app.config['DYNAMO_TABLES'] = [
    {
         TableName:'users',
         KeySchema:[dict(AttributeName='username', KeyType='HASH')],
         AttributeDefinitions:[dict(AttributeName='username', AttributeType='S')],
         ProvisionedThroughput:dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }, {
         TableName:'groups',
         KeySchema:[dict(AttributeName='name', KeyType='HASH')],
         AttributeDefinitions:[dict(AttributeName='name', AttributeType='S')],
         ProvisionedThroughput:dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }
 ]

#create tables
#with app.app_context():
#    dynamo.create_all()
