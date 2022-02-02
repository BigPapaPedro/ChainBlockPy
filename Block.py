import copy
import time


class Block:

    def __init__(self, txns, prevHash, forger, blkCount):

        self.txns = txns
        self.prevHash = prevHash
        self.forger = forger
        self.blkCount = blkCount
        self.timeStamp = time.time()
        self.signature = ''

    @staticmethod
    def genesis():

        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timeStamp = 0

        return genesisBlock

    def payload(self):

        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''

        return jsonRepresentation

    # Sign the block.
    def sign(self, signature):

        self.signature = signature

    # Return the block in JSON format.
    # Have to do it manually since returning self.__dict__ returns the object and not the data.
    def toJson(self):
        # Transaction dictionary.
        data = {}

        data['prevHash'] = self.prevHash
        data['forger'] = self.forger
        data['blkCount'] = self.blkCount
        data['timeStamp'] = self.timeStamp
        data['signature'] = self.signature

        jsonTxns = []

        for txn in self.txns:
            jsonTxns.append(txn.toJson())

        data['txns'] = jsonTxns

        return data