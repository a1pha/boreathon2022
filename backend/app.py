from flask import Flask, request
from flask_dynamo import Dynamo

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
