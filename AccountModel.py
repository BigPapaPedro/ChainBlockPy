class AccountModel:

    def __init__(self):

        # List of public keys of all participants.
        self.accounts = []
        self.balances = {}

    #
    def addAccount(self, pubKeyString):

        if not pubKeyString in self.accounts:

            self.accounts.append(pubKeyString)
            self.balances[pubKeyString] = 0

    #
    def getBalance(self, pubKeyString):

        if pubKeyString not in self.accounts:

                self.addAccount(pubKeyString)

        return self.balances[pubKeyString]

    def updateBalance(self, pubKeyString, amount):

        if pubKeyString not in self.accounts:

            self.addAccount(pubKeyString)

        self.balances[pubKeyString] += amount