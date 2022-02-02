import pprint

from Block import Block
from BlockchainUtils import BlockchainUtils


class BlockChain:

    def __init__(self):

        self.blocks = [Block.genesis()]

    # Add a block to the chain.
    def addBlock(self, block):

        self.blocks.append(block)

    # Validate block count.
    def blockCountValid(self, block):

        # If the previous block count in the chain matches the current block count -1,
        # then it's a valid block.
        if self.blocks[-1].blkCount == block.blkCount - 1:
            return True
        else:
            return False

    #
    def prevBlockHashValid(self, block):

        prevBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

        pprint.pprint(prevBlockchainBlockHash)
        print(block.prevHash)

        if prevBlockchainBlockHash == block.prevHash:
            return True
        else:
            return False

    #
    def toJson(self):

        # Block dictionary.
        data = {}

        jsonBlocks = []

        for block in self.blocks:

            jsonBlocks.append(block.toJson())

        data['blocks'] = jsonBlocks

        return data
