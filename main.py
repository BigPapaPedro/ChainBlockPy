from Node import Node
import sys


if __name__ == '__main__':

    # P2P
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # API port number
    apiPort = int(sys.argv[3])

    # File to private key to create node.
    keyFile = None

    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(apiPort)

