class TransactionPool:

    def __init__(self):

        self.txns = []

    # Add a transaction to the transaction pool.
    def addTxn(self, txn):

        self.txns.append(txn)

    # Verify the transaction does not already exist in the transaction pool.
    def txnExists(self, txn):

        # Iterate through the transaction ppl
        for poolTxn in self.txns:

            if poolTxn.equals(txn):
                return True

        return False

    # Clear the transaction pool.
    def removeFromPool(self, txns):

        newPoolTxns = []

        for poolTxn in self.txns:
            insert = True
            for txn in txns:
                if poolTxn.equals(txn):
                    insert = False

            if insert == True:
                newPoolTxns.append(poolTxn)

        self.txns = newPoolTxns

    # Determine if a new block needs to be forged.
    def forgingRequired(self):

        if len(self.txns) >= 3:
            return True
        else:
            return False

