from TransactionPool import TransactionPool
from Wallet import Wallet
from BlockChain import BlockChain


class Node:

    def __init__(self):

        # Initialize.
        self.txnPool = TransactionPool()
        self.wallet = Wallet()
        self.blockChain = BlockChain()
