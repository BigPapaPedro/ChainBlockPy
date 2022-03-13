from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


if __name__ == '__main__':

    exchange = Wallet()
    alice = Wallet()
    bob = Wallet()

    txn = exchange.createTransaction(exchange.pubKeyString(), 1000000, 'EXCHANGE')
    url = 'http://blockabees.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}
    print('pkg:' + str(pkg))
    req = requests.post(url, json=pkg)
    print(req.text)

    txn = exchange.createTransaction(alice.pubKeyString(), 22, 'EXCHANGE')
    url = 'http://blockabees.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}
    print('pkg:' + str(pkg))
    req = requests.post(url, json=pkg)
    print(req.text)

    txn = exchange.createTransaction(bob.pubKeyString(), 333, 'EXCHANGE')
    url = 'http://blockabees.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}
    print('pkg:' + str(pkg))
    req = requests.post(url, json=pkg)
    print(req.text)

    txn = exchange.createTransaction(exchange.pubKeyString(), 4444, 'EXCHANGE')
    url = 'http://blockabees.sytes.net:8021/txn'
    pkg = {'txn': BlockchainUtils.encode(txn)}
    print('pkg:' + str(pkg))
    req = requests.post(url, json=pkg)
    print(req.text)