from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


if __name__ == '__main__':

    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    txn = exchange.createTransaction(alice.pubKeyString(), 10, 'EXCHANGE')

    url = 'http://localhost:5001/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}

    req = requests.post(url, json=pkg)

    print('req.text')
    print(req.text)

'''
    txn = exchange.createTransaction(alice.pubKeyString(), 10, 'STAKE')

    url = 'http://localhost:5001/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}

    req = requests.post(url, json=pkg)

    print('req.text')
    print(req.text)
'''
