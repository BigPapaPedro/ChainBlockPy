import json
import hashlib


class BlockchainUtils:

    # Takes any type of data and returns in hash.
    @staticmethod
    def hash(data: str):

        # see if it can be done in one line.
        # hashlib.sha256(str.encode())
        # https://www.geeksforgeeks.org/sha-in-python/
        # https://docs.python.org/3/library/hashlib.html

        # Convert data into string.
        dataString = json.dumps(data)

        # Encode the string into bytes.
        dataBytes = dataString.encode('utf-8')

        # Hash the bytes.
        dataHash = hashlib.sha256(dataBytes)

        return dataHash


