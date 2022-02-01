import rsa
from BlockchainUtils import BlockchainUtils
import pkcs


class Wallet:

    def __init__(self):

        (pubKey, privKey) = rsa.newkeys(1024)

    def sign(self, data):

        # TODO: https://servicenow.udemy.com/course/build-your-own-proof-of-stake-blockchain/learn/lecture/23314432#overview
        # PKCS

        dataHash = BlockchainUtils.hash(data)

        return dataHash
