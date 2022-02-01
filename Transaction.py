import uuid
import time


class Transaction():

    def __init__(self, sndrPubKey, rcvrPubKey, amount, txnType):

        self.id = uuid.uuid1()
        self.txnType = txnType
        self.amount = amount
        self.timeStamp = time.time()
        self.sndrPubKey = sndrPubKey
        self.rcvrPubKey = rcvrPubKey
        self.signature = ''

    def toJson(self):

        return self.__dict__
