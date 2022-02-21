from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


if __name__ == '__main__':

    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    txn = exchange.createTransaction(bob.pubKeyString(), 100, 'EXCHANGE')

    print('txn: ' + str(txn.toJson()))

    url = 'http://pedroruiz.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}

    print('pkg:' + str(pkg))

    req = requests.post(url, json=pkg)

    #print(req.text)
'''
    txn = exchange.createTransaction(exchange.pubKeyString(), 1000, 'EXCHANGE')

    url = 'http://pedroruiz.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}

    print(pkg)

    req = requests.post(url, json=pkg)

    #print(req.text)

    txn = exchange.createTransaction(exchange.pubKeyString(), 10000, 'EXCHANGE')

    url = 'http://pedroruiz.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}

    print(pkg)

    req = requests.post(url, json=pkg)

    #print(req.text)
'''