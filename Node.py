import copy

from BlockchainUtils import BlockchainUtils
from Message import Message
from TransactionPool import TransactionPool
from Wallet import Wallet
from BlockChain import BlockChain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from DBDriver import DBDriver


class Node:

    #
    def __init__(self, ip, p2pPort, apiPort, dbName, key=None):

        # Initialize.
        self.ip = ip
        self.p2pPort = p2pPort
        self.apiPort = apiPort
        self.dbName = dbName
        self.txnPool = TransactionPool()
        self.wallet = Wallet()
        self.blockChain = BlockChain()
        self.p2p = None
        self.api = None
        self.db = None

        # Create a wallet using the provided key from file.
        if key is not None:
            self.wallet.fromKey(key)

    #
    def startDB(self):

        self.db = DBDriver(self.dbName)
        self.db.createDB()

    #
    def startP2P(self):

        self.p2p = SocketCommunication(self.ip, self.p2pPort)
        self.p2p.startSocketCommunication(self)

    #
    def startAPI(self):

        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(self.ip, self.apiPort)

    #
    def handleTxn(self, txn):

        data = txn.payload()
        signature = txn.signature
        signerPubKey = txn.sndrPubKey
        signatureValid = Wallet.signatureValid(data, signature, signerPubKey)
        txnExists = self.txnPool.txnExists(txn)
        txnInBlock = self.blockChain.transactionExists((txn))

        if not txnExists and not txnInBlock and signatureValid:
            self.txnPool.addTxn(txn)
            msg = Message(self.p2p.socketConnector, 'TRANSACTION', txn)
            encodedMessage = BlockchainUtils.encode(msg)
            forgingRequired = self.txnPool.forgingRequired()

            # Broadcast the encoded transaction to all nodes.
            self.p2p.broadcast(encodedMessage)

            # Determine if a new block needs to be forged.
            if forgingRequired:
                self.forge()

    #
    def handleBlock(self, block):

        forger = block.forger
        blockHash = block.payload()
        signature = block.signature

        blockCountValid = self.blockChain.blockCountValid(block)
        lastBlockHashValid = self.blockChain.prevBlockHashValid(block)
        forgerValid = self.blockChain.forgeValid(block)
        txnValid = self.blockChain.txnValid(block.txns)
        signatureValid = Wallet.signatureValid(blockHash, signature, forger)

        if not blockCountValid:
            self.requestChain()

        if lastBlockHashValid and forgerValid and txnValid and signatureValid:
            self.blockChain.addBlock(block)
            self.txnPool.removeFromPool(block.txns)
            msg = Message(self.p2p.socketConnector, 'BLOCK', block)
            encodedMsg = BlockchainUtils.encode(msg)
            self.p2p.broadcast(encodedMsg)

    # Request the entire chain.
    def requestChain(self):

        msg = Message(self.p2p.socketConnector, "BLOCKCHAINREQ", None)
        encodedMsg = BlockchainUtils.encode(msg)
        self.p2p.broadcast(encodedMsg)

    #
    def handleBlockchainReq(self, requestingNode):

        msg = Message(self.p2p.socketConnector, 'BLOCKCHAIN', self.blockChain)
        encodedMsg = BlockchainUtils.encode(msg)
        self.p2p.send(requestingNode, encodedMsg)

    #
    def handleBLockchain(self, blockchain):

        localBlockchainCopy = copy.deepcopy(self.blockChain)
        localBlockCount = len(localBlockchainCopy.blocks)
        receivedChainBlockCount = len(blockchain.blocks)

        if localBlockCount < receivedChainBlockCount:

            for blockMember, block in enumerate(blockchain.blocks):

                if blockNumber >= localBlockCount:

                    localBlockchainCopy.addBlock(block)
                    self.txnPool.removeFromPool(block.txns)

            self.blockChain = localBlockchainCopy

    #
    def forge(self):

        forger = self.blockChain.nextForger()

        if forger == self.wallet.pubKeyString():
            print('Im the next forger')

            # Create the block.
            block = self.blockChain.createBlock(self.txnPool.txns, self.wallet)

            # Broadcast the block to the nodes.
            msg = Message(self.p2p.socketConnector, 'BLOCK', block)
            encodedMsg = BlockchainUtils.encode(msg)
            self.p2p.broadcast(encodedMsg)

            # Save the block to the database.
            print("insert block into chain")
            self.db.insertBlock(block)

            # Remove the transactions from the pool.
            self.txnPool.removeFromPool(block.txns)

        else:
            print('Im not the next forger')
