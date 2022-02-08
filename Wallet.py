from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block


class Wallet:

    def __init__(self):

        # Generate public and private key pair.
        self.keyPair = RSA.generate(2048)

        # Extract the public and private keys.
        #self.pubKey = self.keyPair.public_key().export_key('PEM').decode('utf-8')
        #self.privKey = self.keyPair.export_key('PEM').decode('utf-8')

    # Extract the key pair from file.
    def fromKey(self, file):

        key = ''

        with open(file, 'r') as keyFile:
            key = RSA.importKey(keyFile.read())

        self.keyPair = key

    #
    def sign(self, data):

        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObj = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObj.sign(dataHash)

        return signature.hex()

    #
    @staticmethod
    def signatureValid(data, signature, pubKeyString):

        # Get the bytes from the signature.
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        pubKey = RSA.importKey(pubKeyString)
        signatureSchemeObj = PKCS1_v1_5.new(pubKey)

        return signatureSchemeObj.verify(dataHash, signature)

    def pubKeyString(self):

        pubKeyString = self.keyPair.public_key().export_key('PEM').decode('utf-8')

        return pubKeyString

    def createTransaction(self, rcvr, amount, txnType):

        txn = Transaction(self.pubKeyString(), rcvr, amount, txnType)
        signature = self.sign(txn.payload())
        txn.sign(signature)

        return txn

    def createBlock(self, txns, prevHash, blkCount):

        block = Block(txns, prevHash, self.pubKeyString(), blkCount)
        signature = self.sign(block.payload())
        block.sign(signature)

        return block
