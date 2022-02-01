from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':

    sndr = 'sender'
    rcvr = 'receiver'
    amount = 1000000
    txnType = 'transfer'

    txn = Transaction(sndr, rcvr, amount, txnType)

    #print(BlockchainUtils.hash(txnType))
    wallet = Wallet()
    signature = wallet.sign(txn.toJson())

    txn.sign(signature.hexdigest())

    print(txn.toJson())
