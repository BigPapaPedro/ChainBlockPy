import requests
from flask import Flask, jsonify, request, render_template
from flask_classful import FlaskView, route
from BlockchainUtils import BlockchainUtils
from SocketCommunication import SocketCommunication

node = None


class NodeAPI(FlaskView):

    #
    def __init__(self):

        self.app = Flask(__name__)

    #
    def start(self, ip, apiPort):

        NodeAPI.register(self.app, route_base='/')
        self.app.run(host=ip, port=apiPort, use_reloader=True)

    #
    def injectNode(self, injectedNode):

        global node
        node = injectedNode

    #
    @route('/', methods=['GET'])
    def indexPage(self):

        return render_template('home.html')

    #
    @route('info', methods=['GET'])
    def info(self):

        return '<!DOCTYPE html><html lang="en"><head><title>ChainBlockPy 0.01</title></head><body>ChainBlockPy 0.01</body></html>', 200

    #
    @route('blockchain', methods=['GET'])
    def blockchain(self):

        return node.blockChain.toJson(), 200

    #
    @route('txnpool', methods=['GET'])
    def txnPool(self):

        txns = {}

        for ctr, transaction in enumerate(node.txnPool.txns):

            txns[ctr] = transaction.toJson()

        return jsonify(txns), 200

    #
    @route('maketxn', methods=['GET'])
    def makeTxn(self):

        return render_template('maketxn.html')

        #

    @route('test', methods=['POST'])
    def test(self):
        print("@route test: " + str(request.data))
        response = str(request.data)
        return jsonify(response), 201

    #
    @route('txn', methods=['POST'])
    def txn(self):

        print("@route request: " + str(request.data))
        values = request.get_json()
        print("@route values: " + str(values))

        # Verify the received string contains json values.
        if not 'txn' in values:
            return 'Missing transaction values.', 400

        # Decode the received json string into an object.
        txn = BlockchainUtils.decode(values['txn'])

        print("decode: " + txn.signature)

        # Handle the transaction.
        node.handleTxn(txn)

        response = {'msg': 'Received transaction'}

        return jsonify(response), 201

    #
    @route('about', methods=['GET'])
    def about(self):

        return render_template('about.html')

    #
    @route('blockchainexplorer', methods=['GET'])
    def blockchainExplorer(self):

        return render_template('blockchainexplorer.html')

    #
    @route('transactionexplorer', methods=['GET'])
    def txnsExplorer(self):

        return render_template('transactionexplorer.html')

    #
    @route('nodeexplorer', methods=['GET'])
    def nodeExplorer(self):

        return render_template('nodeexplorer.html')
