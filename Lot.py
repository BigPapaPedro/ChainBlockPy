from BlockchainUtils import BlockchainUtils


class Lot:

    def __init__(self, pubKey, iteration, prevBlockHash):

        self.pubKey = str(pubKey)
        self.iteration = iteration
        self.prevBlockHash = prevBlockHash

    #
    def lotHash(self):

        hashData = self.pubKey + self.prevBlockHash

        for _ in range(self.iteration):

            hashData = BlockchainUtils.hash(hashData).hexdigest()

        return hashData