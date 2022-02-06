from Node import Node
import sys


if __name__ == '__main__':

    # P2P
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # API port number
    apiPort = int(sys.argv[3])

    node = Node(ip, port)
    node.startP2P()
    node.startAPI(apiPort)

