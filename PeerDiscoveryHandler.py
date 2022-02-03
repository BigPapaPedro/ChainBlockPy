import threading
import time

from BlockchainUtils import BlockchainUtils
from Message import Message


class PeerDiscoveryHandler:

    def __init__(self, node):

        self.socketCommunication = node

    #
    def start(self):

        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()

    #
    def status(self):

        while True:

            print('Current Connections:')
            for peer in self.socketCommunication.peers:

                print(str(peer.ip) + ':' + str(peer.port))

            time.sleep(10)

    # Discover other nodes in the network.
    def discovery(self):

        while True:

            handshakeMsg = self.handshakeMsg()
            self.socketCommunication.broadcast(handshakeMsg)
            time.sleep(10)

    #
    def handshake(self, node):

        handshakeMsg = self.handshakeMsg()
        self.socketCommunication.send(node, handshakeMsg)

    #
    def handshakeMsg(self):

        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        msgType = 'DISCOVERY'
        msg = Message(ownConnector, msgType, data)
        encodedMsg = BlockchainUtils.encode(msg)

        return encodedMsg

    #
    def handleMsg(self, msg):

        peersSocketConnector = msg.sndrConnector
        peersPeerList = msg.data
        newPeer = True

        for peer in self.socketCommunication.peers:

            if peer.equals(peersSocketConnector):

                newPeer = False

        # if it's a new peer, add it to the peer list.
        if newPeer == True:

            self.socketCommunication.peers.append(peersSocketConnector)

        for peersPeer in peersPeerList:

            peerKnown = False
            for peer in self.socketCommunication.peers:

                if peer.equals(peersPeer):

                    peerKnown = True

            # Make sure it's not sending message to itself.
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):

                self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)