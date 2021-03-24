#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install flask-restful
#pip install eth_account
from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
import algosdk
from flask import Flask


# In[2]:


# In[3]:


#content ={'person_id': '201019',
#    'birthplace':
#        {'country': 'Italy',
#         'city': 'Rome',
#         'year': '1970'}}
#birthplace = json.dumps(content['birthplace'])


# In[ ]:


app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    content = request.get_json(silent=True)   
    
    result = False
    sig = content['sig']
    payload = content['payload']
    platform == content['payload']['platform']
    message = json.dumps(content['payload'])
    pk = payload['pk']

    
    #1. Verifying an endpoint for verifying signatures for ethereum
    if platform == "Ethereum":

        #eth_account.Account.enable_unaudited_hdwallet_features()
        #acct, mnemonic = eth_account.Account.create_with_mnemonic()

        #eth_pk = acct.address
        #eth_sk = acct.key

        #payload = "Sign this!"

        eth_encoded_msg = eth_account.messages.encode_defunct(text=message)
        eth_sig_obj = eth_account.Account.sign_message(eth_encoded_msg,sig)
        print( eth_sig_obj.messageHash )
        result = eth_account.Account.recover_message(eth_encoded_msg,signature=sig)
        if(result ==pk):
            print( "Eth sig verifies!" )    
    
    #2. Verifying an endpoint for verifying signatures for Algorand
    elif platform == "Algorand":
        result=algosdk.util.verify_bytes(message.encode('utf-8'),sig,pk)
        if(result):
            print( "Algo sig verifies!" )
    
    #3. Check for invalid input
    else:
        print("invalid input")

    #Check if signature is valid
    #result = True #Should only be true if signature validates
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')


# In[ ]:




