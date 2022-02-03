from BlockChain import BlockChain
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from AccountModel import AccountModel
import pprint


if __name__ == '__main__':

    blockChain = BlockChain()
    txnPool = TransactionPool()

    # Wallets
    exchange = Wallet()
    alice = Wallet()
    bob = Wallet()
    forger = Wallet()

    exchangeTxn = exchange.createTransaction(alice.pubKeyString(), 10, 'EXCHANGE')

    if not txnPool.txnExists(exchangeTxn):
        txnPool.addTxn(exchangeTxn)

    coveredTxn = blockChain.getCoveredTxnSet(txnPool.txns)
    prevHash = BlockchainUtils.hash(blockChain.blocks[-1].payload()).hexdigest()
    blockCount = blockChain.blocks[-1].blockCount + 1
    blockOne = forger.createBlock(coveredTxn, prevHash, blockCount)
    blockChain.addBlock(blockOne)

    txnPool.removeFromPool(blockOne.txns)

    # alice send 25 tokens to bob
    txn = alice.createTransaction(bob.pubKeyString(), 5, 'TRANSFER')

    if not txnPool.txnExists(txn):
        txnPool.addTxn(txn)

    coveredTxn = blockChain.getCoveredTxnSet(txnPool.txns)
    prevHash = BlockchainUtils.hash(blockChain.blocks[-1].payload()).hexdigest()
    blockCount = blockChain.blocks[-1].blockCount + 1
    blockTwo = forger.createBlock(coveredTxn, prevHash, blockCount)
    blockChain.addBlock(blockTwo)

    txnPool.removeFromPool(blockTwo.txns)

    pprint.pprint(blockChain.toJson())
