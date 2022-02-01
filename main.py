from Transaction import Transaction


if __name__ == '__main__':

    sndr = 'sender'
    rcvr = 'receiver'
    amount = 1000000
    txnType = 'transfer'

    txn = Transaction(sndr, rcvr, amount, txnType)

    print(txn.toJson())