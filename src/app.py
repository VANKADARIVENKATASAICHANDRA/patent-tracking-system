import json
from flask import Flask,request,render_template
from web3 import Web3,HTTPProvider
import urllib3


blockchain='http://127.0.0.1:7545'

def connect():
    web3=Web3(HTTPProvider(blockchain))
    web3.eth.defaultAccount=web3.eth.accounts[0]

    artifact="../build/contracts/Patent.json"
    with open(artifact) as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return contract,web3

app=Flask(__name__)


@app.route('/addPatent', methods=['GET', 'POST'])
def addPatent():
    print("inside addpatent")
    id = int(request.args.get('id'))  # Patent ID
    title = request.args.get('title')  # Patent title
    description = request.args.get('description')  # Patent description
    owner = request.args.get('owner')  # Owner address
    
    contract, web3 = connect()  # Connect to contract and blockchain
    try:
        # Call registerPatent function from the contract
        tx_hash = contract.functions.registerPatent(id, title, description, owner).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'Patent added successfully. Transaction hash: ' + tx_hash.hex()
    except :
        return 'Transaction error'
    

@app.route('/updateOwner', methods=['GET', 'POST'])
def updateOwner():
    id = int(request.args.get('id'))  # Patent ID
    new_owner = request.args.get('new_owner')  # New owner address
    
    contract, web3 = connect()  # Connect to contract and blockchain
    
    try:
        # Call transferOwnership function from the contract
        tx_hash = contract.functions.transferOwnership(id, new_owner).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'Ownership updated successfully. Transaction hash: ' + tx_hash.hex()
    except:
        return 'Transaction error'



@app.route('/verifyPatent', methods=['GET'])
def verifyPatent():
    id = int(request.args.get('id'))  # Patent ID
    
    contract, web3 = connect()  # Connect to contract and blockchain
    
    try:
        # Call verifyPatent function from the contract
        patent = contract.functions.verifyPatent(id).call()
        return {
            'id': patent[0],
            'title': patent[1],
            'description': patent[2],
            'owner': patent[3],
            'isActive': patent[4]
        }
    except Exception as e:
        return 'Error verifying patent: ' + str(e)


@app.route('/',methods=['GET','POST'])
def addpatent():
    return render_template('addpatent.html')
@app.route('/verifypatentpage',methods=['GET','POST'])
def verifypatentpage():
    return render_template('verifypatent.html')

@app.route('/updateownerpage',methods=['GET','POST'])
def updateownerpage():
    return render_template('updateowner.html')

@app.route('/addpatentform',methods=['GET','POST'])
def addpatentform():
    # print("id->"+request.form['id'])
    id=request.form['id']
    title=request.form['title']
    description =request.form['description']
    owner=request.form['owner']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:5002/addPatent?id='+id+'&title='+title+'&description='+description+'&owner='+owner)
    response=response.data
    response=response.decode('utf-8')
    return render_template('addpatent.html',response=response)


@app.route('/verifypatentform',methods=['GET','POST'])
def verifypatentform():
    id=request.form['id']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:5002/verifyPatent?id='+id)
    response=response.data
    response=response.decode('utf-8')
    return render_template('verifypatent.html',response=response)

@app.route('/updateownerform',methods=['GET','POST'])
def updateownerform():
    id=request.form['id']
    address=request.form['new_owner']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:5002/updateOwner?id='+id+'&new_owner='+address)
    response=response.data
    response=response.decode('utf-8')
    return render_template('updateowner.html',response=response)





if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5002,
        debug=True
    )