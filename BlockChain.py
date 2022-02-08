import pprint
from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake

class BlockChain:

    def __init__(self):

        # Initialize block with the genesis block.
        self.blocks = [Block.genesis()]

        # Initialize the account model.
        self.acntModel = AccountModel()

        self.pos = ProofOfStake()

    # Add a block to the chain.
    def addBlock(self, block):

        self.executeTxns(block.txns)
        self.blocks.append(block)

    # Validate block count.
    def blockCountValid(self, block):

        # If the previous block count in the chain matches the current block count -1,
        # then it's a valid block.
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

    #
    def prevBlockHashValid(self, block):

        prevBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

        if prevBlockchainBlockHash == block.prevHash:
            return True
        else:
            return False

    #
    def getCoveredTxnSet(self, txns):

        coveredTransactions = []

        for txn in txns:
            if self.txnCovered(txn):
                coveredTransactions.append(txn)
            else:
                print('Transaction is not covered by sender.')

        return coveredTransactions

    # See if the sender has sufficient tokens to cover the transaction amount.
    def txnCovered(self, txn):

        if txn.txnType == 'EXCHANGE':
            return True

        sndrBalance = self.acntModel.getBalance(txn.sndrPubKey)

        if sndrBalance >= txn.amount:
            return True
        else:
            return False

    #
    def executeTxns(self, txns):

        for txn in txns:
            self.executeTxn(txn)

    #
    def executeTxn(self, txn):

        print(txn.toJson())

        if txn.txnType =='STAKE':

            sndr = txn.sndrPubKey
            rcvr = txn.rcvrPubKey

            if sndr == rcvr:

                amount = txn.amount
                self.pos.update(sndr, amount)
                self.acntModel.updateBalance(sndr, -amount)

            else:

                sndr = txn.sndrPubKey
                rcvr = txn.rcvrPubKey
                amount = txn.amount

                self.acntModel.updateBalance(sndr, -amount)
                self.acntModel.updateBalance(rcvr, amount)

    #
    def nextForger(self):

        prevBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

        nextForger = self.pos.forger(prevBlockHash)

        return nextForger

    #
    def createBlock(self, txnsFromPool, forgerWallet):

        coveredTxns = self.getCoveredTxnSet(txnsFromPool)

        self.executeTxns(coveredTxns)
        newBlock = forgerWallet.createBlock(coveredTxns, BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest(), len(self.blocks))
        self.blocks.append(newBlock)

        return newBlock

    # Determine if the transaction is already in the blockchain
    # by searching the transaction in the blockchain.
    # (I don't think this will scale well as the blockchain grows.)
    def transactionExists(self, txn):

        for block in self.blocks:

            for blockTxn in block.txns:

                if txn.equals(blockTxn):

                    return True

        return False

    #
    def forgeValid(self, block):

        forgePubKey = self.pos.forger(block.prevHash)
        proposedBlockForger = block.forger

        if forgePubKey == proposedBlockForger:
            return True
        else:
            return False

    #
    def txnValid(self, txns):

        coveredTxns = self.getCoveredTxnSet(txns)

        if len(coveredTxns) == len(txns):
            return True

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
