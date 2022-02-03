from BlockChain import BlockChain
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from AccountModel import AccountModel
from Node import Node
import sys
import pprint


if __name__ == '__main__':

    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2p()

    print(node.blockChain)
    print(node.txnPool)
    print(node.wallet)

