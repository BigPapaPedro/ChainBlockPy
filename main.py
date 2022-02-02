from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

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
    signature = wallet.sign(txn.payload())

    # Validate the signature.
    signatureValid = Wallet.signatureValid(txn.payload(), txn.signature, wallet.pubKeyString())

    #print(signatureValid)
    print(txn.toJson())

    print(txnPool.txnPool)
