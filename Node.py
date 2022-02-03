from TransactionPool import TransactionPool
from Wallet import Wallet
from BlockChain import BlockChain
from SocketCommunication import SocketCommunication


class Node:

    def __init__(self, ip, port):

        # Initialize.
        self.p2p = Node
        self.ip = ip
        self.port = port
        self.txnPool = TransactionPool()
        self.wallet = Wallet()
        self.blockChain = BlockChain()

    #
    def startP2p(self):

        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication()