import copy
import uuid
import time


class Transaction:

    def __init__(self, sndrPubKey, rcvrPubKey, amount, txnType):

        self.id = uuid.uuid1().hex
        self.txnType = txnType
        self.amount = amount
        self.timeStamp = time.time()
        self.sndrPubKey = sndrPubKey
        self.rcvrPubKey = rcvrPubKey
        self.signature = ''

    # Set the signature value of the transaction
    def sign(self, signature):

        self.signature = signature

    # Make a copy of the transaction, clear the signature if its set and return the modified copy.
    def payload(self):

        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''

        return jsonRepresentation

    # Return the dictionary in JSON format.
    def toJson(self):

        return self.__dict__
