import json

from p2pnetwork.node import Node

from BlockchainUtils import BlockchainUtils
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector


class SocketCommunication(Node):

    # Initialize socket communications.
    def __init__(self, ip, port):

        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)

    # Start socket communication.
    def startSocketCommunication(self, node):

        self.node = node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToGenesisNode()

    #
    def connectToGenesisNode(self):

        if self.socketConnector.port != 8081:
            self.connect_with_node('localhost', 8081)

    #
    def inbound_node_connected(self, connectedNode):

        print('Inbound Node ' + str(connectedNode.port) + ' connected.')
        self.peerDiscoveryHandler.handshake(connectedNode)

    #
    def outbound_node_connected(self, connectedNode):

        print('Outbound Node ' + str(connectedNode.port) + ' connected.')
        self.peerDiscoveryHandler.handshake(connectedNode)

    #
    def node_message(self, node, msg):

        msg = BlockchainUtils.decode(json.dumps(msg))

        if msg.msgType == 'DISCOVERY':

            self.peerDiscoveryHandler.handleMsg((msg))

        elif msg.msgType== 'TRANSACTION':

            txn = msg.data
            self.node.handleTxn(txn)

    #
    def send(self, rcvr, msg):

        self.send_to_node(rcvr, msg)

    #
    def broadcast(self, msg):

        self.send_to_nodes(msg)
