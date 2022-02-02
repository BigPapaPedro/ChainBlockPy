from Crypto.Hash import SHA256
import json


class BlockchainUtils:

    # Takes any type of data and returns in hash.
    @staticmethod
    def hash(data: str):

        # Convert data into string.
        dataString = json.dumps(data)

        # Encode the string into bytes.
        dataBytes = dataString.encode('utf-8')

        # Hash the bytes.
        dataHash = SHA256.new(dataBytes)

        return dataHash
