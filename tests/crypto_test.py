from brownie import *
from eth_account import Account, messages

def test_ecrecover():
    contract = accounts[0].deploy(ECRecover)
    account = Account.create()
    message = messages.encode_defunct(text="ilovebrownie")
    messageHash = messages.defunct_hash_message(message.body)
    signature = account.sign_message(message)
    (v,r,s) = (signature.v, signature.r, signature.s)
    assert contract.foo(messageHash,v,r,s) == account.address
    
def test_keccak256():
    contract = accounts[0].deploy(Hash)
    message = b"potato"
    assert contract.foo(message) == "0x9e159dfcfe557cc1ca6c716e87af98fdcb94cd8c832386d0429b2b7bec02754f"