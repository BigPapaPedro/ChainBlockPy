import requests
from flask import Flask, jsonify, request
from flask_classful import FlaskView, route
from BlockchainUtils import BlockchainUtils

node = None


class NodeAPI(FlaskView):

    #
    def __init__(self):

        self.app = Flask(__name__)

    #
    def start(self, apiPort):

        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='localhost', port=apiPort)

    #
    def injectNode(self, injectedNode):

        global node
        node = injectedNode

    #
    @route('/info', methods=['GET'])
    def info(self):

        return 'This is a communication interface to a nodes blockchain', 200

    #
    @route('/blockchain', methods=['GET'])
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
    @route('txn', methods=['POST'])
    def txn(self):

        values = request.get_json()

        # Verify the received string contains json values.
        if not 'txn' in values:
            return 'Missing transaction values.', 400

        # Decode the received json string into an object.
        txn = BlockchainUtils.decode(values['txn'])

        # Handle the transaction.
        node.handleTxn(txn)

        response = {'msg': 'Received transaction'}

        return jsonify(response), 201
    