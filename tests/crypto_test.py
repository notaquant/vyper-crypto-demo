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
    
def test_hash():
    contract = accounts[0].deploy(Hash)
    message = b"potato"
    assert contract.foo(message) == "0x9e159dfcfe557cc1ca6c716e87af98fdcb94cd8c832386d0429b2b7bec02754f"

def test_bls():
    contract = accounts[0].deploy(BLS)
    G1 = (1,2)
    G2 = [[11559732032986387107991004021392285783925812861821192530917403151452391805634,
            10857046999023057135944570762232829481370756359578518086990519993285655852781],[4082367875863433681332203403145435568316851327593401208105741076214120093531,
            8495653923123431417604973247489272438418190587263600148770280649306958101930]]
    assert G1 == contract.P1() and G2 == contract.P2()