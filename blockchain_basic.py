import datetime
import random
import hashlib
import json
from flask import Flask, jsonify


class blockchain:
        def __init__(self):
                self.chain=[]
                self.create_block(proof=1,prev_hash=0)

        def create_block(self,proof,prev_hash):
                block={"index":len(self.chain)+1, "timestamp":str(datetime.datetime.now()), "proof":proof,"prev_hash":prev_hash}
                self.chain.append(block)
                return block
        
        def get_last_block(self):
                return self.chain[-1]
        
        def proof_of_work(self):
                new_proof=1
                pow_state=False
                while pow_state is False:
                        s = new_proof**(random.randint(0,9)) 
                        n = hashlib.sha256(str(s).encode()).hexdigest()
            
                        if n[:4]== "0000":
                                pow_state = True
                        else:
                                new_proof+=1
                return new_proof
    
        def mine(self):
                prv=json.dumps(self.get_last_block())
                prv_hsh = hashlib.sha256(prv.encode()).hexdigest()
                p = self.proof_of_work()
                new_ch=self.create_block(p,prv_hsh)
                #print(new_ch)
                return 'Successfully mined'
        
        def show_chain(self):
                return self.chain


a=blockchain()
app = Flask(__name__)
@app.route('/mine')
def minee():
        return a.mine()

@app.route('/show_chain')
def shw_chain():
        return json.dumps((a.show_chain()))

