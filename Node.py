from BlockchainUtils import BlockchainUtils
from Message import Message
from TransactionPool import TransactionPool
from Wallet import Wallet
from BlockChain import BlockChain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI


class Node:

    #
    def __init__(self, ip, port):

        # Initialize.
        self.ip = ip
        self.port = port
        self.p2p = None
        self.txnPool = TransactionPool()
        self.wallet = Wallet()
        self.blockChain = BlockChain()
        self.api = None

    #
    def startP2P(self):

        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

    #
    def startAPI(self, apiPort):

        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    #
    def handleTxn(self, txn):

        data = txn.payload()
        signature = txn.signature
        signerPubKey = txn.sndrPubKey
        signatureValid = Wallet.signatureValid(data, signature, signerPubKey)
        txnExists = self.txnPool.txnExists(txn)

        if not txnExists and signatureValid:
            self.txnPool.addTxn(txn)
            msg = Message(self.p2p.socketConnector, 'TRANSACTION', txn)
            encodedMessage = BlockchainUtils.encode(msg)
            self.p2p.broadcast(encodedMessage)
