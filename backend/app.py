from flask import Flask, request
from flask_dynamo import Dynamo
from boto3.session import Session()

boto_sess = Session(
    region_name='us-east-1',
    aws_access_key_id='example_key_id',
    aws_secret_access_key='my_super_secret_key'
)
app.config['DYNAMO_SESSION'] = boto_sess



app = Flask(__name__)


@app.route('/api/CustomerAccount/GetCustomerAccountByAccountNumber', methods=['GET'])
def retrieveAccountDetails():


@app.route('/api/CustomerAccount/OpenCustomerAccount', methods=['POST'])
def openAccount():
    req = request.json


@app.route('/api/CustomerAccount/CloseCustomerAccount', methods=['POST'])
def closeAccount():
    req = request.json


@app.route('/api/CustomerAccount/ApplyTransactionToCustomerAsync', methods=['POST'])
def applyTransaction():
    req = request.json 

    # Credit
    if req['transactionType'] == 1:

    # Debit
    if req['transactionType'] == 0:
