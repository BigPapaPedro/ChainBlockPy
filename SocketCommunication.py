import json

from p2pnetwork.node import Node

from BlockchainUtils import BlockchainUtils
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector


class SocketCommunication(Node):

    # Initialize socket communications.
    def __init__(self, ip, port):

        super(SocketCommunication, self).__init__(ip, port, Node)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)
    #
    def connectToGenesisNode(self):

        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost', 10001)

    # Start socket communication.
    def startSocketCommunication(self):

        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToGenesisNode()

    #
    def inbound_node_connected(self, node):

        self.peerDiscoveryHandler.handshake(node)

    #
    def outbound_node_connected(self, node):

        self.peerDiscoveryHandler.handshake(node)

    #
    def inbound_node_disconnected(self, node):

        print('Node ' + str(node.port) + ' disconnected.')

    #
    def node_message(self, node, msg):

        # Decode the incoming message.
        msg = BlockchainUtils.decode(json.dumps(msg))

        if msg.msgType == 'DISCOVERY':

            self.peerDiscoveryHandler.handleMsg(msg)

    # Send a message to a node.
    def send(self, rcvr, msg):

        self.send_to_node(rcvr, msg)

    # Broadcast a message to all nodes.
    def broadcast(self, msg):

        self.send_to_nodes(msg)
