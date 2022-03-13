from Lot import Lot
from BlockchainUtils import BlockchainUtils


class ProofOfStake:

    def __init__(self):

        self.stakers = {}
        self.setGenesisNodeStake()

    #
    def setGenesisNodeStake(self):

        genesisPubKey = open('keys/genesisPublicKey.pem', 'r').read()
        #genesisPubKey = open('keys/genesisPublicKey.der', 'r').read()
        self.stakers[genesisPubKey] = 1

    #
    def update(self, pubKeyString, stake):

        # Only add the pubKey if not already in it.
        if pubKeyString in self.stakers.keys():

            self.stakers[pubKeyString] += stake

        else:

            self.stakers[pubKeyString] = stake

    # Generate one lot per stake.
    def get(self, pubKeyString):

        if pubKeyString in self.stakers.keys():

            return self.stakers[pubKeyString]

        else:

            return None

    #
    def validatorLots(self, seed):

        lots = []

        for validator in self.stakers.keys():

            for stake in range(self.get(validator)):

                lots.append(Lot(validator, stake + 1, seed))

        return lots

    #
    def winnerLot(self, lots, seed):

        winnerLot = None
        leastOffset = None

        refHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)

        for lot in lots:

            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - refHashIntValue)

            if leastOffset is None or offset < leastOffset:

                leastOffset = offset
                winnerLot = lot

        return winnerLot

    #
    def forger(self, prevBlockHash):

        lots = self.validatorLots(prevBlockHash)
        winnerLot = self.winnerLot(lots, prevBlockHash)

        return winnerLot.pubKey
