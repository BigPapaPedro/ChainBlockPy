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

    print(sys.path)

    #
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # API
    apiPort = int(sys.argv[3])

    node = Node(ip, port)
    node.startP2p()
    node.startAPI()

