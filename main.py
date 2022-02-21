from Node import Node
import sys


if __name__ == '__main__':

    dbName = "sample.db"

    # IP or URL
    ip = sys.argv[1]

    # P2P
    p2pPort = int(sys.argv[2])

    # API port number
    apiPort = int(sys.argv[3])

    # File with private key to create node.
    keyFile = None

    # Since the keyfile is optional, check if one was given.
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    # Create an instance of the node and start the services.
    node = Node(ip, p2pPort, apiPort, dbName, keyFile)
    node.startDB()
    node.startP2P()
    node.startAPI()
