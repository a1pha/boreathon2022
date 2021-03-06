from flask import Flask, request
from flask_dynamo import Dynamo
import boto3
import random

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
    response = userTable.get_item(Key={'associated_account' : str(account_num)})
    response2 = accountTable.get_item(Key={'account_number' : str(account_num)})
    return str(response['Item']) + " " + str(response2['Item'])


@app.route('/api/CustomerAccount/OpenCustomerAccount', methods=['POST'])
def openAccount():
    args = request.args
    firstname = args.get("firstName") 
    lastname = args.get("lastName") 

    accountID = int(random.randint(0, 10000))
    print(accountID)


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
    return "Added user " + accountID


@app.route('/api/CustomerAccount/CloseCustomerAccount', methods=['POST'])
def closeAccount():
    args = request.args
    accountNo = args.get("accountNumber") 
    accountTable.delete_item(
    Key={
        'account_number': str(accountNo)
    })
    userTable.delete_item(
    Key={
        'associated_account': str(accountNo)
    }
)



    return "Success"


@app.route('/api/CustomerAccount/ApplyTransactionToCustomerAsync', methods=['POST'])
def applyTransaction():
    args = request.args
    accountNo = args.get("accountNumber") 
    transAmount = args.get("transaction_amount")
    transType = args.get("transaction_type")
    
    # Credit
    if transType == 1:
        return ""

    # Debit
    if transType == 0:

        return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0')