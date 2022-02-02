

class TransactionPool:

    def __init__(self):

        self.txnPool = []

    # Add a transaction to the transaction pool.
    def addTxn(self, txn):

        self.txnPool.append(txn)

    # Verify the transaction does not already exist in the transaction pool.
    def txnExists(self, txn):

        # Iterate through the transaction ppl
        for poolTxn in self.txnPool:

            if poolTxn.equals(txn):
                return True

        return False


