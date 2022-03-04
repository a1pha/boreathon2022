from flask import Flask, request
from flask_dynamo import Dynamo
import boto3
from random import random

# boto_sess = Session(
#     region_name='us-east-1',
#     aws_access_key_id='example_key_id',
#     aws_secret_access_key='my_super_secret_key'
# )
# app.config['DYNAMO_SESSION'] = boto_sess
AWS_ACCESS_KEY_ID = 'AKIAWLU3NUWTE3BD7VN6'
AWS_SECRET_ACCESS_KEY = 'PHtQY2qLpZlHcMT4ig/no4pv0T9Acre50aI1rx7m'
REGION_NAME = 'us-east-2'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key= AWS_SECRET_ACCESS_KEY, region_name = REGION_NAME)

accountTable = dynamodb.Table('R3-Account')

userTable = dynamodb.Table('R3-Customer')

transactionTable = dynamodb.Table('R3-Transaction')


app = Flask(__name__)

accountID = 1




@app.route('/', methods=['GET'])
def hello():
    return "Hello, world!"


@app.route('/api/CustomerAccount/GetCustomerAccountByAccountNumber', methods=['GET'])
def retrieveAccountDetails():
    args = request.args
    account_num = args.get("accountNumber") 
    userTable.get_item(Key={'account_number' : str(account_num)})


    return account_num


@app.route('/api/CustomerAccount/OpenCustomerAccount', methods=['POST'])
def openAccount():
    args = request.args
    firstname = args.get("firstName") 
    lastname = args.get("lastName") 

    accountID = int(random.random()*1000)


    accountTable.put_item(
   Item={
        'ID': accountID,
        'account_number': str(accountID),
        'balance': 10000,
        'account_status': 1,
    })

    userTable.put_item(
   Item={
        'ID': accountID,
        'firstName': firstname,
        'lastName': lastname,
        'associated_account': str(accountID)    ,
    })
    accountID += 1
    return "Added user"


@app.route('/api/CustomerAccount/CloseCustomerAccount', methods=['POST'])
def closeAccount():
    args = request.args
    accountNo = args.get("accountNumber") 
    accountTable.delete_item(
    Key={
        'account_Number': str(accountNo)
    })
    userTable.delete_item(
    Key={
        'associated_account': str(accountNo)
    }
)



    return "Success"


@app.route('/api/CustomerAccount/ApplyTransactionToCustomerAsync', methods=['POST'])
def applyTransaction():
    req = request.json 

    # Credit
    if req['transactionType'] == 1:
        return ""

    # Debit
    if req['transactionType'] == 0:

        return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0')