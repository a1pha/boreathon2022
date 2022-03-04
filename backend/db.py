from flask import Flask
from flask_dynamo import Dynamo
from app.py import app #fix this import

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

app.config['DYNAMO_TABLES'] = [
    {
         TableName:'R3-Account',
         KeySchema:[dict(AttributeName='ID', KeyType='HASH')],
         AttributeDefinitions:[
		dict(AttributeName='ID', AttributeType='N'),
		dict(AttributeName='accountNum', AttributeType='S'),
		dict(AttributeName='balance', AttributeType='N'),
		dict(AttributeName='accountStatus', AttributeType='S')
	 ],
         ProvisionedThroughput:dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }, {
         TableName:'R3-Customer',
         KeySchema:[dict(AttributeName='ID', KeyType='HASH')],
         AttributeDefinitions:[
		dict(AttributeName='ID', AttributeType='N'),
		dict(AttributeName='firstName', AttributeType='S'),
		dict(AttributeName='lastName', AttributeType='S'),
		dict(AttributeName='associatedAcc', AttributeType='S')
	 ],
         ProvisionedThroughput:dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }, {
         TableName:'R3-Transaction',
         KeySchema:[dict(AttributeName='ID', KeyType='HASH')],
         AttributeDefinitions:[
		dict(AttributeName='ID', AttributeType='N'),
		dict(AttributeName='amount', AttributeType='N'),
		dict(AttributeName='transactionType', AttributeType='S'),
		dict(AttributeName='associatedAcc', AttributeType='S')
	 ],
         ProvisionedThroughput:dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
    }

 ]

#create tables
#with app.app_context():
#    dynamo.create_all()
