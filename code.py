5.3.1 Hash.py
from hashlib import sha256
import json
import time
class Hash:
def __init__(self, index, transactions, timestamp, previous_hash):
self.index = index
self.transactions = transactions
self.timestamp = timestamp
self.previous_hash = previous_hash
self.nonce = 0
def compute_hash(self):
"""
A function that return the hash of the block contents.
"""
block_string = json.dumps(self.__dict__, sort_keys=True)
return sha256(block_string.encode()).hexdigest()

5.3.2 Validate.py
from hashlib import sha256
import json
import time
import pickle
from datetime import datetime
import random
import base64
from Hash import *
class Validate:
# difficulty of our PoW algorithm
difficulty = 2 #using difficulty 2 computation
def __init__(self):
self.unconfirmed_transactions = []
self.chain = []
self.create_genesis_block()
self.peer = []
self.translist = []
def create_genesis_block(self): #create genesis block
genesis_block = Block(1, [], time.time(), "3")
genesis_block.hash = genesis_block.compute_hash()
self.chain.append(genesis_block)
def last_block(self):
return self.chain[-1]
def add_block(self, block, proof): #adding data to block by computing new and previous hashes
previous_hash = self.last_block.hash
if previous_hash != block.previous_hash:
return False
if not self.is_valid_proof(block, proof):
return False
block.hash = proof
#print("main "+str(block.hash))
self.chain.append(block)
return True
def is_valid_proof(self, block, block_hash): #proof of work
return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash ==
block.compute_hash())
def proof_of_work(self, block): #proof of work
block.nonce = 0
computed_hash = block.compute_hash()
while not computed_hash.startswith('0' * Blockchain.difficulty):
block.nonce += 1
computed_hash = block.compute_hash()
return computed_hash
def add_new_transaction(self, transaction):
self.unconfirmed_transactions.append(transaction)
def addPeer(self, peer_details):
self.peer.append(peer_details)
def addTransaction(self,trans_details): #add transaction
self.translist.append(trans_details)
def mine(self):#mine transaction
if not self.unconfirmed_transactions:
return False
last_block = self.last_block
new_block = Block(index=last_block.index ,
transactions=self.unconfirmed_transactions,
timestamp=time.time(),
previous_hash=last_block.hash)
proof = self.proof_of_work(new_block)
self.add_block(new_block, proof)
self.unconfirmed_transactions = []
return new_block.ind
def save_object(self,obj, filename):
with open(filename, 'wb') as output:
pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

5.3.3 Main.py:
from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from Hash import *
from Validate import *
from hashlib import sha256
import os
main = Tk()
main.title("CERTIFICATE STORAGE AND VALIDATION")
main.geometry("1200x1200")
global filename
blockchain = Blockchain()
if os.path.exists('blockchain_contract.txt'):
with open('blockchain_contract.txt', 'rb') as fileinput:
blockchain = pickle.load(fileinput)
fileinput.close()
def Tenth():
global filename
filename = askopenfilename(initialdir = "certificate_templates")
with open(filename,"rb") as f:
bytes = f.read()
f.close()
roll_no = tf1.get()
name = tf2.get()
contact = tf3.get()
if len(roll_no) > 0 and len(name) > 0 and len(contact) > 0:
digital_signature = sha256(bytes).hexdigest();
data = roll_no+"#"+name+"#"+contact+"#"+digital_signature
blockchain.add_new_transaction(data)
hash = blockchain.mine()
b = blockchain.chain[len(blockchain.chain)-1]
text.insert(END,"Previous Hash : "+str(b.previous_hash)+"\nCurrent Hash : "+str(b.hash)+"\n")
text.insert(END,"Certificate Digital Signature : "+str(digital_signature)+"\n\n")
blockchain.save_object(blockchain,'blockchain_contract.txt')
else:
text.insert(END,"Please enter Roll No")
def Inter():
global filename
filename = askopenfilename(initialdir = "certificate_templates")
with open(filename,"rb") as f:
bytes = f.read()
f.close()
roll_no = tf1.get()
name = tf2.get()
contact = tf3.get()
if len(roll_no) > 0 and len(name) > 0 and len(contact) > 0:
digital_signature = sha256(bytes).hexdigest();
data = roll_no+"#"+name+"#"+contact+"#"+digital_signature
blockchain.add_new_transaction(data)
hash = blockchain.mine()
b = blockchain.chain[len(blockchain.chain)-1]
text.insert(END,"Previous Hash : "+str(b.previous_hash)+"\nCurrent Hash : "+str(b.hash)+"\n")
text.insert(END,"Certificate Digital Signature : "+str(digital_signature)+"\n\n")
blockchain.save_object(blockchain,'blockchain_contract.txt')
else:
text.insert(END,"Please enter Roll No")
def Btech():
global filename
filename = askopenfilename(initialdir = "certificate_templates")
with open(filename,"rb") as f:
bytes = f.read()
f.close()
roll_no = tf1.get()
name = tf2.get()
contact = tf3.get()
if len(roll_no) > 0 and len(name) > 0 and len(contact) > 0:
digital_signature = sha256(bytes).hexdigest();
data = roll_no+"#"+name+"#"+contact+"#"+digital_signature
blockchain.add_new_transaction(data)
hash = blockchain.mine()
b = blockchain.chain[len(blockchain.chain)-1]
text.insert(END,"Previous Hash : "+str(b.previous_hash)+"\nCurrent Hash : "+str(b.hash)+"\n")
text.insert(END,"Certificate Digital Signature : "+str(digital_signature)+"\n\n")
blockchain.save_object(blockchain,'blockchain_contract.txt')
else:
text.insert(END,"Please enter Roll No")
def verifyCertificate():
filename = askopenfilename(initialdir = "certificate_templates")
with open(filename,"rb") as f:
bytes = f.read()
f.close()
digital_signature = sha256(bytes).hexdigest();
flag=True
for i in range(len(blockchain.chain)):
if i > 0:
b = blockchain.chain[i]
data = b.transactions[0]
arr = data.split("#")
if arr[3] == digital_signature:
text.insert(END,"\nUploaded Certificate Validation Successfull\n")
text.insert(END,"Details after Validation\n\n")
text.insert(END,"Roll No : "+arr[0]+"\n")
text.insert(END,"Student Name : "+arr[1]+"\n")
text.insert(END,"Contact No : "+arr[2]+"\n")
text.insert(END,"Digital Sign : "+arr[3]+"\n")
flag = False
break
if flag:
text.insert(END,"\n\nVerification failed or certificate modified")
font = ('times', 15, 'bold')
title = Label(main, text='CERTIFICATE STORAGE AND VALIDATION')
title.config(bg='blue4', fg='white')
title.config(font=font)
title.config(height=3, width=130)
title.place(x=0,y=5)
font1 = ('times', 13, 'bold')
l1 = Label(main, text='Roll No :')
l1.config(font=font1)
l1.place(x=50,y=100)
tf1 = Entry(main,width=20)
tf1.config(font=font1)
tf1.place(x=180,y=100)
l2 = Label(main, text='Student Name :')
l2.config(font=font1)
l2.place(x=50,y=150)
tf2 = Entry(main,width=20)
tf2.config(font=font1)
tf2.place(x=180,y=150)
l3 = Label(main, text='Contact No :')
l3.config(font=font1)
l3.place(x=50,y=200)
tf3 = Entry(main,width=20)
tf3.config(font=font1)
tf3.place(x=180,y=200)
saveButton = Button(main, text="Tenth certificate", command=Tenth)
saveButton.place(x=50,y=250)
saveButton.config(font=font1)
saveButton = Button(main, text="Inter certificate", command=Inter)
saveButton.place(x=250,y=250)
saveButton.config(font=font1)
saveButton = Button(main, text="Btech certificate", command=Btech)
saveButton.place(x=450,y=250)
saveButton.config(font=font1)
verifyButton = Button(main, text="Verify Certificate", command=verifyCertificate)
verifyButton.place(x=720,y=250)
verifyButton.config(font=font1)
font1 = ('times', 13, 'bold')
text=Text(main,height=15,width=120)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=300)
text.config(font=font1)
main.config(bg='LightSteelBlue2')
