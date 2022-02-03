from p2pnetwork.node import Node


class SocketCommunication(Node):

    # Initialize socket communications.
    def __init__(self, ip, port):

        super(SocketCommunication, self).__init__(ip, port, Node)

    # Start socket communication.
    def startSocketCommunication(self):

        self.start()
