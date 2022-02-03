from BlockChain import BlockChain
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block

import pprint


if __name__ == '__main__':

    sndr = 'sender'
    rcvr = 'receiver'
    amount = 1000000
    txnType = 'TRANSFER'

    # Create a wallet.
    # This is how transactions are created.
    wallet = Wallet()
    txnPool = TransactionPool()

    # Create a transaction.
    txn = wallet.createTransaction(rcvr, amount, txnType)

    if txnPool.txnExists(txn) == False:
        txnPool.addTxn(txn)

    # Generate the signature for the transaction.
    #signature = wallet.sign(txn.payload())

    blockChain = BlockChain()

    prevHash = BlockchainUtils.hash(blockChain.blocks[-1].payload()).hexdigest()
    blockCount = blockChain.blocks[-1].blkCount + 1
    block = wallet.createBlock(txnPool.txnPool, prevHash, blockCount)

    if not blockChain.prevBlockHashValid(block):
        print('Previous block hash is not valid.')

    if not blockChain.blockCountValid(block):
        print('Block count is not valid.')

    if blockChain.prevBlockHashValid(block) and blockChain.blockCountValid(block):
        blockChain.addBlock(block)

    pprint.pprint(blockChain.toJson())
